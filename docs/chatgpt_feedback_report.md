# Hackathon Progress Report for ChatGPT

*Context for ChatGPT: We are exactly 1 hour into a 30-hour hackathon for the Sohjo Hacks "Language Station for Multilingual Pedagogy" challenge. We have already designed, scoped, and built a fully functioning Minimum Viable Product (MVP) based on your previous advice. We want you to audit our progress and tell us exactly what we should spend the next 29 hours doing to guarantee a win, without breaking our solid foundation.*

---

## 1. Our Concept: "The Cognitive Multilingual Toolkit"
We built a web dashboard for university lecturers. They upload a dense, monolingual academic text or PDF, and the tool returns a tailored, multilingual lesson kit focusing on translanguaging and cognitive load reduction.

## 2. Our Tech Stack & Architecture
- **Language:** Python 3.10+
- **Frontend:** Streamlit (clean, modern, tabbed UI)
- **Backend LLM:** Google Gemini (`gemini-2.5-flash` natively, accessed via `google-generativeai`)
- **JSON Framework:** Pydantic (using Gemini's native Structured Outputs via `response_schema` to guarantee perfect JSON parsing every time)
- **Document Parsing:** `PyMuPDF` (for PDF uploads)

## 3. What We Have Built In Hour 1
We locked the LLM into a strict "One Call, One JSON Output" structure. The pipeline accepts text, truncates it to the first 15,000 characters for safety, and sends a single prompt to Gemini (with `temperature=0.4` for academic consistency).

The Streamlit UI has a Sidebar for uploading `.txt` or `.pdf` files, and a toggle to switch between **Fast Mode (gemini-2.5-flash)** and **High Quality (gemini-2.5-pro)**. 

When generated, the UI outputs 3 distinct tabs:

### Tab 1: 📚 Cognitive Glossary
We parse the LLM's selected difficult academic terminology. Instead of a boring table, we render custom HTML/CSS Markdown cards for each word containing:
- The Term (bold)
- Finnish translation (italicized)
- A simple CEFR A2/B1 definition
- **Our Edge:** A "Cognitive Note" (a 1-sentence explanation of the word's polysemy, metaphor, or specific semantic variation in this academic context vs. everyday use).

### Tab 2: 🌉 Bilingual Bridge
A side-by-side view using Streamlit columns. 
- Left: The original dense academic text.
- Right: A complete rewrite simplified to a CEFR B1 level that retains the core academic concepts but strips out complex syntax.

### Tab 3: 🗓️ Pedagogy Planner
An accordion (Streamlit expanders) containing 2-3 specific, 5-10 minute classroom activities specifically tailored to the uploaded text that encourage **translanguaging** (e.g., instructing students to discuss the English text in Finnish before summarizing).

---

## 4. Our Question for You (ChatGPT)
**We finished the MVP in 1 hour. We have 29 hours left.** 
We do not want to succumb to feature creep or overengineering that breaks our clean demo. 

Given our current state:
1. What should we spend "Day 2" doing? 
2. What specific UX polish, evaluation metrics, or feature additions (e.g., specific prompting changes, caching, RAG?) would take this from a "great MVP" to an "undeniable 1st place winner"?
3. How should we structure the rest of our time?
