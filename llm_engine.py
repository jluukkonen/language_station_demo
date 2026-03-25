import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables locally
load_dotenv()

# Initialize Gemini client (check OS env first, fallback to Streamlit secrets)
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
genai.configure(api_key=api_key)

# Verified terminology dictionary sourced from FINTO (Finnish Thesaurus and Ontology Service) / MeSH
VERIFIED_TERMS = {
    "pathogenesis": "patogeneesi",
    "epidemiology": "epidemiologia",
    "microbiology": "mikrobiologia",
    "etiology": "etiologia",
    "diagnosis": "diagnoosi",
    "prognosis": "ennuste",
    "staphylococcus aureus": "Staphylococcus aureus",
    "nosocomial infection": "sairaalainfektio",
    "multidrug-resistant": "moniresistentti",
    "morbidity": "sairastavuus",
    "mortality": "kuolleisuus",
    "evidence-based": "näyttöön perustuva"
}

class GlossaryItem(BaseModel):
    term: str = Field(description="A short academic term or key phrase (strictly 1 to 4 words max) extracted from the source text.")
    academic_definition: str = Field(description="A concise academic definition of the term.")
    simple_definition: str = Field(description="A simple A2/B1 level explanation of the term.")
    cognitive_note: str = Field(description="A 1-sentence note explaining any polysemy or semantic variation (everyday vs. academic use).")
    # Added post-generation via static mapping
    finnish_translation: Optional[str] = Field(description="Leave this blank. System will populate this.")

class PedagogySuggestion(BaseModel):
    activity_name: str = Field(description="The catchy name of the translanguaging classroom activity.")
    instructions: str = Field(description="Step-by-step instructions for the teacher on how to run this activity using the provided text.")

class LanguageStationOutput(BaseModel):
    glossary: List[GlossaryItem] = Field(description="A list of 5-8 key academic terms extracted from the text.")
    simplified_text: str = Field(description="The entire original text rewritten at a CEFR B1 level.")
    pedagogy_suggestions: List[PedagogySuggestion] = Field(description="2-3 collaborative, group-based translanguaging activities based on the text.")

def get_system_prompt() -> str:
    """Reads the system prompt from system_prompt.txt."""
    prompt_path = os.path.join(os.path.dirname(__file__), "prompts", "system_prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def process_text(text: str, model_type: str = "gemini-2.5-flash", input_mode: str = "Use course material", language_direction: str = "English → Finnish") -> LanguageStationOutput:
    """
    Processes the raw input using Google Gemini Structured Outputs.
    Adapts to 'Course Material' or 'Lesson Description' modes.
    Implements bidirectional (EN<->FI) terminology verification.
    """
    # Truncate to ~4000 words / 15000 chars
    truncated_text = text[:15000]
    
    system_prompt = get_system_prompt()
    
    # Context Injection for the LLM
    context_prefix = f"### TASK CONTEXT ###\nInput Mode: {input_mode}\nLanguage Focus: {language_direction}\n\n"
    
    # Initialize the model with the response schema
    model = genai.GenerativeModel(model_name=model_type)
    
    # Use explicit GenerationConfig for safety rails
    generation_config = genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema=LanguageStationOutput,
        temperature=0.4
    )
    
    # Combine context, system prompt and user input
    full_prompt = f"""
{context_prefix}
{system_prompt}

--- USER INPUT START ---
{truncated_text}
--- USER INPUT END ---
"""
    
    response = model.generate_content(
        full_prompt,
        generation_config=generation_config
    )
    
    # Parse the JSON response
    try:
        json_data = json.loads(response.text)
        result = LanguageStationOutput(**json_data)
        
        # Surgical Pivot: Deterministic Bidirectional Translation Mapping
        for item in result.glossary:
            term_key = item.term.lower().strip()
            found = False

            if language_direction == "English → Finnish":
                # Normal Lookup (Key -> Value)
                if term_key in VERIFIED_TERMS:
                    item.finnish_translation = VERIFIED_TERMS[term_key]
                    found = True
                else:
                    for key, val in VERIFIED_TERMS.items():
                        if key in term_key:
                            item.finnish_translation = val
                            found = True
                            break
            
            else:
                # Reverse Lookup (Value -> Key) for Finnish → English
                # We still store it in the 'finnish_translation' field because the Pydantic schema is fixed
                # The UI will label it correctly based on the mode.
                for key, val in VERIFIED_TERMS.items():
                    if val.lower() == term_key or val.lower() in term_key:
                        item.finnish_translation = key # This is the English equivalent
                        found = True
                        break
            
            if not found:
                item.finnish_translation = "Not found in verified terminology"
        
        return result
    except Exception as e:
        # Prevent UnboundLocalError if response failed completely
        raw = response.text if 'response' in locals() else str(e)
        # Fallback error handling
        return LanguageStationOutput(
            glossary=[],
            simplified_text=f"⚠️ Processing Error: {raw}",
            pedagogy_suggestions=[]
        )

if __name__ == "__main__":
    # Test script
    test_text = "Cognitive linguistics is an interdisciplinary branch of linguistics."
    try:
        result = process_text(test_text)
        print("Success! Parsed Output:")
        print(result.model_dump_json(indent=2))
    except Exception as e:
        print(f"Error: {e}")
