# Instructions for Junior Dev (Gemini Flash): Final Performance Tweaks

**Context:**
The app is working perfectly, but we need to optimize the LLM engine for cost, speed, and output consistency based on our latest hackathon strategy.

**Your Tasks:**
1. **Update `llm_engine.py`:**
   - Change the `model_name` in `genai.GenerativeModel` from `"gemini-1.5-flash"` to `"gemini-2.5-flash"`.
   - Add `"temperature": 0.4` to the `generation_config` dictionary. Lowering the temperature is critical to ensure the JSON structure remains uncorrupted and the glossary definitions remain objective and academic, rather than overly creative.

2. **(Optional Bonus) Update `app.py` UI Toggle:**
   - If you have time, add a `st.sidebar.radio` or `st.sidebar.selectbox` in `app.py` that lets the user toggle between "Fast Mode (gemini-2.5-flash)" and "High Quality (gemini-2.5-pro)". 
   - Pass this selection down to `process_text()` in `llm_engine.py` so the judges can see that the UI dynamically supports both speed and deep academic rigor.

Execute these updates and we are ready for the final pitch!
