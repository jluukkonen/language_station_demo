# Instructions for Junior Dev (Gemini Flash)

**Context for Flash:**
We are in a 30-hour hackathon building the "Language Station," a Cognitive Multilingual Toolkit for university lecturers. The tool takes dense academic text, extracts complex terms, translates them (English ↔ Finnish), simplifies the text to CEFR B1, and generates translanguaging lesson activities. 

All planning is completed. Your job is to execute the Python and Streamlit code.

---

## Technical Stack & Requirements
- **Language:** Python 3.10+
- **Libraries:** `streamlit`, `openai` (v1.0+), `python-dotenv`, `pydantic`.
- **Architecture:** We are using **OpenAI Structured Outputs** (passing a Pydantic model to `client.beta.chat.completions.parse`) to guarantee perfect JSON responses every single time. 

---

## Step 1: The Core Pipeline (`llm_engine.py`)
Write a Python module that takes a raw text string and passes it to the OpenAI API (using `gpt-4o-mini` or `gpt-4o`).
1. Read the system prompt from the `system_prompt.txt` file we already created.
2. Define a Pydantic class `LanguageStationOutput` that exactly matches the JSON schema expected in `system_prompt.txt`. 
3. Create a function `process_text(text: str) -> dict` that handles the API call and returns the parsed JSON dictionary.

## Step 2: The Streamlit App (`app.py`)
Write a clean, modern Streamlit UI. 
- **Header:** Title it "Language Station: Cognitive Multilingual Toolkit".
- **Sidebar:** Include a file uploader (for `.txt` for now) and a text area for direct copy-pasting existing syllabus text. Include a big "Generate Lesson Kit" button.
- **Main Content Area:** Once generated, display the results in 3 Tabs using `st.tabs`:
    - **Tab 1: Cognitive Glossary.** Display the extracted terms, standard definitions, Finnish translations, and the unique cognitive/semantic notes as a clean table or set of markdown cards.
    - **Tab 2: Bilingual Bridge.** Use `st.columns(2)` to show the original text on the left and the CEFR-simplified B1 text on the right.
    - **Tab 3: Pedagogy Planner.** Display the suggested translanguaging classroom activities using `st.expander` or markdown bullet points.

## Instructions on how to start:
1. Generate the `requirements.txt`.
2. Generate the code for `llm_engine.py`.
3. Generate the code for `app.py`.
4. Keep the UI extremely clean, using Streamlit's native components to mimic a polished dashboard. Do not overcomplicate the logic—this is a hackathon MVP.
