# Instructions for Junior Dev (Gemini Flash): Migrate to Gemini

**Context for Flash:**
The user has decided to switch the LLM backend from OpenAI to Google Gemini. 

Your tasks are:
1. **Update `requirements.txt`:** Remove `openai` and add `google-genai` (the official SDK for Gemini, or `google-generativeai` if you are using the older v1 API).
2. **Update `.env.example`:** Change `OPENAI_API_KEY` to `GEMINI_API_KEY`.
3. **Refactor `llm_engine.py`:**
   - Initialize the Gemini API client instead of OpenAI using `GEMINI_API_KEY`.
   - Keep all the Pydantic classes identical (`GlossaryItem`, `PedagogySuggestion`, `LanguageStationOutput`).
   - Use the Gemini 2.5 Flash model (or Gemini 1.5 Pro) to generate the content. 
   - Gemini natively supports Structured Outputs! Pass your Pydantic `LanguageStationOutput` schema directly to the `response_schema` parameter in the `generate_content` call, and set `response_mime_type="application/json"`. 
   - *Crucial:* Keep the `text[:15000]` truncation limit intact to ensure safety during the demo.
4. Do not touch `app.py` or the UI at all. This should just be a seamless brain transplant.

Please rewrite `llm_engine.py`, `requirements.txt`, and `.env.example` and execute them now.
