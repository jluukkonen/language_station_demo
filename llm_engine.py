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
    "pathogenesis": "patogeneesi",  # Source: MeSH
    "epidemiology": "epidemiologia",  # Source: MeSH
    "microbiology": "mikrobiologia",  # Source: Finto
    "etiology": "etiologia",  # Source: MeSH
    "diagnosis": "diagnoosi",  # Source: Finto
    "prognosis": "ennuste",  # Source: Finto
    "evidence-based": "näyttöön perustuva",  # Source: Finto
    "nosocomial infection": "sairaalainfektio",  # Source: MeSH
    "staphylococcus aureus": "Staphylococcus aureus",  # Source: MeSH
    "multidrug-resistant": "moniresistentti",  # Source: MeSH
    "morbidity": "sairastavuus",  # Source: MeSH
    "mortality": "kuolleisuus",  # Source: MeSH
    "clinical trial": "kliininen koe",  # Source: MeSH
    "randomized controlled trial": "satunnaistettu kontrolloitu koe",  # Source: MeSH
    "systematic review": "systemaattinen katsaus",  # Source: MeSH
    "meta-analysis": "meta-analyysi",  # Source: MeSH
    "prevalence": "esiintyvyys",  # Source: MeSH
    "incidence": "ilmenemistiheys",  # Source: MeSH
    "risk factor": "riskitekijä",  # Source: MeSH
    "comorbidity": "sairastavuus",  # Source: MeSH
    "clinical guideline": "kliininen ohjeistus",  # Source: MeSH
    "patient outcome": "potilaan hoitotulos",  # Source: Finto
    "intervention": "interventio",  # Source: MeSH
    "assessment": "arviointi",  # Source: Finto
    "healthcare": "terveydenhuolto",  # Source: Finto
    "nursing care": "hoitotyö",  # Source: Finto
    "medication": "lääkehoito",  # Source: Finto
    "surgery": "kirurgia",  # Source: MeSH
    "rehabilitation": "kuntoutus",  # Source: Finto
    "infection control": "infektiontorjunta",  # Source: Finto
    "patient safety": "potilasturvallisuus",  # Source: Finto
    "health promotion": "terveyden edistäminen",  # Source: Finto
    "diagnostic test": "diagnostinen testi",  # Source: Finto
    "laboratory work": "laboratoriotyö",  # Source: Finto
    "simulation": "simulaatio",  # Source: Finto
    "flipped learning": "flipped learning",  # Source: Pedagogical terminology
    "interactive learning": "vuorovaikutteinen oppiminen",  # Source: Finto
    "evidence synthesis": "näyttöön perustuva synteesi",  # Source: MeSH
    "public health": "kansanterveys",  # Source: MeSH
    "primary care": "perusterveydenhuolto",  # Source: MeSH
    "secondary care": "erikoissairaanhoito",  # Source: Finto
    "tertiary care": "kolmannen asteen hoito",  # Source: Finto
    "clinical reasoning": "kliininen päättely",  # Source: Finto
    "interprofessional education": "ammatillinen monialaopetus",  # Source: Finto
    "qualitative research": "kvalitatiivinen tutkimus",  # Source: Finto
    "quantitative research": "kvantitatiivinen tutkimus",  # Source: Finto
    "methodology": "menetelmätiede",  # Source: Finto
    "theoretical framework": "teoreettinen viitekehys",  # Source: Finto
    "case study": "tapaustutkimus",  # Source: Finto
    "literature review": "kirjallisuuskatsaus",  # Source: Finto
    "synthesis": "synteesi",  # Source: Finto
    "evidence": "näyttö",  # Source: Finto
    "protocol": "protokolla",  # Source: MeSH
    "triage": "triage",  # Source: MeSH
    "health assessment": "terveystarkastus",  # Source: Finto
    "vital signs": "elintoiminnot",  # Source: Finto
    "pathology": "patologia",  # Source: MeSH
    "pharmacology": "farmakologia",  # Source: MeSH
    "immunology": "immunologia",  # Source: MeSH
    "cardiology": "kardiologia",  # Source: MeSH
    "neurology": "neurologia",  # Source: MeSH
    "oncology": "onkologia",  # Source: MeSH
    "pediatrics": "lastentautioppi",  # Source: MeSH
    "geriatrics": "geriatriikka",  # Source: MeSH
    "psychiatry": "psykiatria",  # Source: MeSH
    "surgery department": "kirurgian osasto",  # Source: Finto
    "nursing department": "hoitotyön osasto",  # Source: Finto
    "infection": "infektio",  # Source: MeSH
    "virus": "virus",  # Source: MeSH
    "bacteria": "bakteeri",  # Source: MeSH
    "fungi": "sieni",  # Source: MeSH
    "parasite": "loinen",  # Source: MeSH
    "diagnostic imaging": "diagnostinen kuvantaminen",  # Source: Finto
    "ultrasound": "ultraääni",  # Source: Finto
    "x-ray": "röntgen",  # Source: Finto
    "magnetic resonance imaging": "magneettikuvaus",  # Source: Finto
    "computed tomography": "tietokonetomografia",  # Source: Finto
    "method": "menetelmä",  # Source: Finto
    "analysis": "analyysi",  # Source: Finto
    "result": "tulos",  # Source: Finto
    "conclusion": "johtopäätös",  # Source: Finto
    "discussion": "keskustelu",  # Source: Finto
    "recommendation": "suositus",  # Source: Finto
    "intervention study": "interventiotutkimus",  # Source: MeSH
    "observational study": "havainnointitutkimus",  # Source: MeSH
    "cohort study": "kohorttitutkimus",  # Source: MeSH
    "case-control study": "tapaus-verrokki-tutkimus",  # Source: MeSH
    "cross-sectional study": "poikkileikkaustutkimus",  # Source: MeSH
    "randomization": "satunnaistaminen",  # Source: Finto
    "blinding": "sokkoutus",  # Source: Finto
    "ethical approval": "eettinen hyväksyntä",  # Source: Finto
    "informed consent": "informed consent",  # Source: Finto
    "confounding factor": "sekoittava tekijä",  # Source: MeSH
    "bias": "harha",  # Source: MeSH
    "statistical significance": "tilastollinen merkitsevyys",  # Source: Finto
    "confidence interval": "luottamusväli",  # Source: Finto
    "p-value": "p-arvo",  # Source: Finto
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
