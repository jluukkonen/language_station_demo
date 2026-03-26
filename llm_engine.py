import os
import json
from typing import Any, Dict, List, Optional
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

# Import the generated large-scale dictionaries (Run generate_dictionaries.py first)
try:
    from verified_academic_dictionaries import (
        MESH_DICTIONARY, 
        TERO_DICTIONARY, 
        OIKO_DICTIONARY,
        LAJISTO_DICTIONARY,
        KASSU_DICTIONARY,
        AFO_DICTIONARY,
        JUPO_DICTIONARY,
        KOKO_DICTIONARY, 
        YSO_DICTIONARY
    )
    # Master Dictionary – Priority (Python unpack overwrites L->R, so highest priority is last):
    # Order: MESH > TERO > OIKO > LAJISTO > KASSU > AFO > JUPO > KOKO > YSO
    VERIFIED_TERMS = {
        **YSO_DICTIONARY, 
        **KOKO_DICTIONARY, 
        **JUPO_DICTIONARY, 
        **AFO_DICTIONARY, 
        **KASSU_DICTIONARY, 
        **LAJISTO_DICTIONARY, 
        **OIKO_DICTIONARY, 
        **TERO_DICTIONARY, 
        **MESH_DICTIONARY
    }
except ImportError:
    # Fallback to empty if not generated yet
    VERIFIED_TERMS = {}

class GlossaryItem(BaseModel):
    term: str = Field(description="A short academic term or key phrase (strictly 1 to 4 words max) extracted from the source text.")
    academic_definition: str = Field(description="A deep, precise academic definition suitable for a university lecturer.")
    simple_definition: str = Field(description="A simple A2/B1 level explanation of the term.")
    cognitive_note: str = Field(description="A 1-sentence note explaining any polysemy or semantic variation (everyday vs. academic use).")
    equivalent_term: str = Field(description="The equivalent term in the target language based on the 'Language Focus' context.")

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

def process_text(
    text: str,
    model_type: str = "gemini-2.5-flash",
    input_mode: str = "Use course material",
    language_direction: str = "English → Finnish",
    selected_students: Optional[List[Dict[str, Any]]] = None,
    selected_course: Optional[Dict[str, Any]] = None
) -> LanguageStationOutput:
    """
    Processes the raw input using Google Gemini Structured Outputs.
    Adapts to 'Course Material' or 'Lesson Description' modes.
    Implements bidirectional (EN<->FI) terminology verification.
    """
    # Truncate to ~4000 words / 15000 chars
    truncated_text = text[:15000]
    
    system_prompt = get_system_prompt()
    
    group_context = ""
    if selected_students:
        group_context = "\n".join([
            f"{s['name']} | CEFR: {s['cefr']} | Schooling: {s['schooling_language']} | Languages: {', '.join(s['linguistic_repertoire'])}"
            for s in selected_students
        ])
        
        # Add linguistic barriers if they exist
        barriers = [f"{s['name']}: {s['linguistic_barrier']}" for s in selected_students if s.get('linguistic_barrier')]
        if barriers:
            group_context += "\n\nLinguistic challenges:\n" + "\n".join(barriers)

    course_context = selected_course["description"] if selected_course else "N/A"

    # Context Injection for the LLM
    context_prefix = (
        f"### TASK CONTEXT ###\n"
        f"Input Mode: {input_mode}\n"
        f"Language Focus: {language_direction}\n"
        f"Course Context: {course_context}\n"
        f"\nGROUPS AND LANGUAGES:\n{group_context}\n"
    )
    
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

Adapt all outputs (especially activities and simplified text) to the group's collective level, programs, and prior knowledge.

You are designing a lesson for a multilingual group of students:
{group_context}

Course context:
{course_context}

Design activities that:
- require collaboration between students
- explicitly use their linguistic repertoires
- implement translanguaging (students must use multiple languages)
- support S2 integration (learning Finnish within subject content)
- are practical and classroom-ready
- reference students explicitly by name (e.g. "Ask Ahmed to explain X to Aino in English before translating to Finnish")

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
        
        # Hybrid Translation Architecture: Verified First → AI Fallback
        for item in result.glossary:
            term_key = item.term.lower().strip()
            verified_value = None

            if language_direction == "English → Finnish":
                # Exact O(1) Lookup (Key -> Value)
                if term_key in VERIFIED_TERMS:
                    verified_value = VERIFIED_TERMS[term_key]
            else:
                # Exact Reverse Lookup (Value -> Key) for Finnish → English
                # Note: We iterate since we don't have a reverse map, but use exact comparison
                for key, val in VERIFIED_TERMS.items():
                    if val.lower() == term_key:
                        verified_value = key
                        break
            
            # Apply Labels: Green for Verified, Orange for AI Fallback
            if verified_value:
                item.equivalent_term = f"{verified_value} 🟢 (Verified)"
            else:
                item.equivalent_term = f"{item.equivalent_term} 🟠 (AI-Assisted)"
        
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
