import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GlossaryItem(BaseModel):
    term: str = Field(description="A short academic term or key phrase (strictly 1 to 4 words max) extracted from the source text.")
    academic_definition: str = Field(description="A concise academic definition of the term.")
    finnish_translation: str = Field(description="The Finnish translation of the term in its specific academic context.")
    simple_definition: str = Field(description="A simple A2/B1 level explanation of the term.")
    cognitive_note: str = Field(description="A 1-sentence note explaining any polysemy or semantic variation (everyday vs. academic use).")

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

def process_text(text: str, model_type: str = "gemini-2.5-flash") -> LanguageStationOutput:
    """
    Processes the raw academic text using Google Gemini Structured Outputs.
    Uses Pydantic Field descriptions and GenerationConfig for maximum robustness.
    """
    # Truncate to ~4000 words / 15000 chars
    truncated_text = text[:15000]
    
    system_prompt = get_system_prompt()
    
    # Initialize the model with the response schema
    model = genai.GenerativeModel(model_name=model_type)
    
    # Use explicit GenerationConfig for safety rails
    generation_config = genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema=LanguageStationOutput,
        temperature=0.4
    )
    
    # Combine system prompt and user text
    full_prompt = f"""
{system_prompt}

--- SOURCE TEXT START ---
{truncated_text}
--- SOURCE TEXT END ---
"""
    
    response = model.generate_content(
        full_prompt,
        generation_config=generation_config
    )
    
    # Parse the JSON response
    try:
        json_data = json.loads(response.text)
        return LanguageStationOutput(**json_data)
    except Exception as e:
        # Fallback error handling
        return LanguageStationOutput(
            glossary=[],
            simplified_text=f"⚠️ Parsing error: Could not generate simplified text. Raw: {response.text}",
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
