# Language Station: MVP & Hackathon Roadmap

## 1. The Core Concept (The Elevator Pitch)
"We built a Language Station that turns any dense course material into a multilingual, pedagogically-informed learning toolkit in seconds. It bridges the gap between NLP and multilingual pedagogy."

## 2. MVP Features (Strictly Enforced Scope)
- **Input:** Upload an academic PDF or paste text.
- **Extract:** 10–20 key terms (using TF-IDF/KeyBERT).
- **Define & Translate:** Generate simple definitions and Finnish translations for those terms.
- **Adapt:** Produce a CEFR-simplified version (e.g., A2/B1 level) of the text.
- **Teach:** Generate 2-3 specific, actionable translanguaging activities.

## 3. The "Edge" (Our Differentiator)
**Linguistically Informed Adaptation:** We don't just translate. We highlight the *semantic variation* and *polysemy* of words depending on their academic context, lowering the cognitive load for non-native speakers.

## 4. System Architecture
```text
[Input Text/PDF] 
       ↓ 
[Term Extraction: KeyBERT / spaCy] 
       ↓ 
[LLM Processing: OpenAI API]
  ├─ Definitions & Translations
  ├─ Text Simplification (CEFR)
  └─ Teaching Suggestions
       ↓ 
[Frontend UI: Streamlit]
```

## 5. UI Layout (Streamlit)
- **Sidebar/Left:** File uploader & raw text view.
- **Main Area (Right):**
  - **Tab 1: Cognitive Glossary** (Terms, translations, contextual meanings).
  - **Tab 2: Bilingual Bridge** (Simplified CEFR text + original).
  - **Tab 3: Lesson Planner** (Translanguaging activities).

## 6. The "Golden" Demo Data
*Do not rely on live, random text during the pitch.* 
We must pre-select 1-2 dense academic texts (e.g., a Linguistics or CS abstract) where we *know* the AI performs beautifully and extracts interesting polysemous words.

## 7. Action Items (Next Steps)
- [ ] Prepare 1 sample "Golden" text for the demo.
- [ ] Setup the Python virtual environment and basic Streamlit `app.py`.
- [ ] Build the term extraction pipeline (spaCy/KeyBERT).
- [ ] Write the LLM prompts for Definitions, Adaptation, and Pedagogy.
