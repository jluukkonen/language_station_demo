import streamlit as st
import pandas as pd
import fitz  # PyMuPDF
import html
from llm_engine import process_text

# Page Config
st.set_page_config(
    page_title="Language Station",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium hackathon demo look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg-main: #f4f7fb;
        --bg-panel: rgba(255, 255, 255, 0.82);
        --bg-card: #ffffff;
        --bg-soft-blue: #eff5ff;
        --bg-soft-green: #effaf4;
        --bg-soft-ink: #eef2f8;
        --text-primary: #152033;
        --text-secondary: #5c6b82;
        --border-soft: rgba(22, 35, 58, 0.09);
        --shadow-soft: 0 18px 45px rgba(23, 37, 84, 0.08);
        --shadow-hover: 0 24px 55px rgba(23, 37, 84, 0.14);
        --blue: #295eef;
        --blue-deep: #183b8c;
        --teal: #0e8aa8;
        --green: #1f9d63;
        --gold: #d9a441;
        --radius-lg: 24px;
        --radius-md: 18px;
        --radius-sm: 14px;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at top left, rgba(41, 94, 239, 0.10), transparent 28%),
            radial-gradient(circle at top right, rgba(14, 138, 168, 0.10), transparent 24%),
            linear-gradient(180deg, #f7faff 0%, #f4f7fb 100%);
    }

    .main .block-container {
        padding-top: 2.2rem;
        padding-bottom: 2rem;
        max-width: 1280px;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fbff 0%, #eef4fb 100%);
        border-right: 1px solid rgba(22, 35, 58, 0.08);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.4rem;
    }

    .sidebar-shell {
        padding: 0.25rem 0 0.65rem 0;
    }

    .sidebar-brand {
        background: linear-gradient(135deg, rgba(41, 94, 239, 0.12), rgba(14, 138, 168, 0.10));
        border: 1px solid rgba(41, 94, 239, 0.10);
        border-radius: 22px;
        padding: 1rem 1rem 0.95rem 1rem;
        box-shadow: var(--shadow-soft);
        margin-bottom: 1rem;
    }

    .sidebar-kicker {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--blue-deep);
        margin-bottom: 0.5rem;
    }

    .sidebar-title {
        font-size: 1.15rem;
        line-height: 1.2;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 0.35rem;
    }

    .sidebar-copy {
        font-size: 0.92rem;
        line-height: 1.55;
        color: var(--text-secondary);
        margin: 0;
    }

    .sidebar-section {
        margin: 1.15rem 0 0.65rem 0;
        font-size: 0.74rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #6b7a90;
    }

    .hero-card {
        position: relative;
        overflow: hidden;
        padding: 2rem 2rem 1.7rem 2rem;
        border-radius: 28px;
        background:
            radial-gradient(circle at 90% 10%, rgba(255, 255, 255, 0.38), transparent 18%),
            linear-gradient(135deg, #173870 0%, #2154b7 42%, #0b8cad 100%);
        box-shadow: 0 28px 70px rgba(24, 59, 140, 0.23);
        border: 1px solid rgba(255, 255, 255, 0.14);
        margin-bottom: 1.5rem;
        color: white;
    }

    .hero-card::after {
        content: "";
        position: absolute;
        inset: auto -80px -120px auto;
        width: 280px;
        height: 280px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.08);
        filter: blur(6px);
    }

    .hero-kicker {
        display: inline-block;
        padding: 0.45rem 0.75rem;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.13);
        border: 1px solid rgba(255, 255, 255, 0.18);
        font-size: 0.76rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: clamp(2.2rem, 4.1vw, 3.7rem);
        line-height: 1.02;
        font-weight: 800;
        margin: 0;
        max-width: 760px;
    }

    .hero-copy {
        margin: 0.95rem 0 1.35rem 0;
        font-size: 1.02rem;
        line-height: 1.7;
        max-width: 760px;
        color: rgba(255, 255, 255, 0.88);
    }

    .hero-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
    }

    .hero-badge {
        padding: 0.58rem 0.88rem;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.16);
        font-size: 0.86rem;
        font-weight: 600;
        color: white;
    }

    .section-intro {
        background: var(--bg-panel);
        backdrop-filter: blur(14px);
        border: 1px solid var(--border-soft);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-soft);
        padding: 1.2rem 1.25rem;
        margin-bottom: 1rem;
    }

    .section-kicker {
        font-size: 0.72rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        font-weight: 700;
        color: var(--blue-deep);
        margin-bottom: 0.45rem;
    }

    .section-title {
        margin: 0;
        color: var(--text-primary);
        font-size: 1.35rem;
        font-weight: 800;
    }

    .section-copy {
        margin: 0.45rem 0 0 0;
        color: var(--text-secondary);
        line-height: 1.65;
        font-size: 0.98rem;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin: 1rem 0 1.4rem 0;
    }

    .stat-card {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid var(--border-soft);
        border-radius: 22px;
        box-shadow: var(--shadow-soft);
        padding: 1.15rem 1.2rem;
    }

    .stat-label {
        color: var(--text-secondary);
        font-size: clamp(0.66rem, 0.61rem + 0.22vw, 0.78rem);
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 0.6rem;
        line-height: 1.35;
    }

    .stat-value {
        color: var(--text-primary);
        font-size: clamp(1.4rem, 1.08rem + 0.9vw, 2rem);
        line-height: 1;
        font-weight: 800;
    }

    .stat-subtle {
        margin-top: 0.45rem;
        color: #718098;
        font-size: 0.92rem;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.85rem;
        padding: 0.25rem 0 0.6rem 0;
    }

    .stTabs [data-baseweb="tab"] {
        height: 56px;
        background: rgba(255, 255, 255, 0.76);
        border: 1px solid var(--border-soft);
        border-radius: 18px;
        padding: 0 1.15rem;
        color: var(--text-secondary);
        font-weight: 700;
        transition: all 0.2s ease;
        box-shadow: none;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-primary);
        border-color: rgba(41, 94, 239, 0.18);
        transform: translateY(-1px);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(180deg, #ffffff 0%, #f4f8ff 100%);
        color: var(--blue-deep);
        border-color: rgba(41, 94, 239, 0.22);
        box-shadow: var(--shadow-soft);
    }

    .glossary-card,
    .planner-card,
    .text-panel {
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid var(--border-soft);
        border-radius: 22px;
        box-shadow: var(--shadow-soft);
        transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
    }

    .glossary-card:hover,
    .planner-card:hover,
    .text-panel:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-hover);
        border-color: rgba(41, 94, 239, 0.14);
    }

    .glossary-card {
        padding: 1.35rem;
        margin-bottom: 1rem;
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(246, 250, 255, 0.96));
    }

    .card-meta {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.55rem;
        margin-bottom: 0.8rem;
    }

    .term-chip,
    .translation-chip,
    .difficulty-chip,
    .planner-chip {
        display: inline-flex;
        align-items: center;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 700;
        padding: 0.45rem 0.72rem;
    }

    .term-chip {
        background: var(--bg-soft-blue);
        color: var(--blue-deep);
    }

    .translation-chip {
        background: #edf8fb;
        color: #0c7087;
    }

    .difficulty-chip {
        background: #fff7ea;
        color: #9a6a00;
    }

    .planner-chip {
        background: #eef7ff;
        color: var(--blue-deep);
        margin-bottom: 0.8rem;
    }

    .term-title {
        color: var(--text-primary);
        font-size: 1.45rem;
        line-height: 1.15;
        font-weight: 800;
        margin: 0 0 0.85rem 0;
    }

    .card-label {
        display: block;
        color: var(--blue-deep);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.32rem;
    }

    .card-copy {
        color: var(--text-primary);
        line-height: 1.72;
        margin: 0 0 0.9rem 0;
        font-size: 0.98rem;
    }

    .cognitive-note {
        margin-top: 0.4rem;
        padding: 0.95rem 1rem;
        border-radius: 16px;
        background: linear-gradient(180deg, #f3f7ff 0%, #edf4ff 100%);
        border: 1px solid rgba(41, 94, 239, 0.10);
        color: #28405f;
        line-height: 1.65;
    }

    .bridge-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
    }

    .text-panel {
        padding: 1.25rem;
        height: 100%;
    }

    .text-panel.original {
        background: linear-gradient(180deg, #ffffff 0%, #f7f9fc 100%);
    }

    .text-panel.simplified {
        background: linear-gradient(180deg, #fcfffd 0%, #f1fbf5 100%);
        border-color: rgba(31, 157, 99, 0.14);
    }

    .panel-label {
        display: inline-block;
        border-radius: 999px;
        padding: 0.45rem 0.72rem;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.85rem;
    }

    .panel-label.original {
        background: var(--bg-soft-ink);
        color: #50627d;
    }

    .panel-label.simplified {
        background: var(--bg-soft-green);
        color: #187b4d;
    }

    .panel-title {
        margin: 0 0 0.6rem 0;
        color: var(--text-primary);
        font-size: 1.15rem;
        font-weight: 800;
    }

    .panel-copy {
        margin: 0;
        color: var(--text-secondary);
        line-height: 1.78;
        font-size: 0.98rem;
        white-space: pre-wrap;
    }

    .planner-card {
        padding: 1.3rem;
        margin-bottom: 1rem;
        background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
    }

    .planner-title {
        margin: 0 0 0.6rem 0;
        color: var(--text-primary);
        font-size: 1.18rem;
        font-weight: 800;
    }

    .planner-copy {
        margin: 0;
        color: var(--text-secondary);
        line-height: 1.72;
        font-size: 0.98rem;
    }

    .status-banner {
        background: linear-gradient(180deg, #f4fcf7 0%, #eefbf4 100%);
        border: 1px solid rgba(31, 157, 99, 0.15);
        color: #176a43;
        border-radius: 18px;
        padding: 0.95rem 1rem;
        box-shadow: var(--shadow-soft);
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .empty-state {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid var(--border-soft);
        border-radius: 24px;
        box-shadow: var(--shadow-soft);
        padding: 1.4rem 1.5rem;
        color: var(--text-secondary);
        line-height: 1.7;
    }

    .footer-note {
        text-align: center;
        color: #6d7b91;
        font-size: 0.9rem;
        padding: 0.5rem 0 0.2rem 0;
    }

    [data-testid="stFileUploader"],
    [data-testid="stTextArea"],
    [data-testid="stRadio"] {
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(22, 35, 58, 0.07);
        border-radius: 18px;
        padding: 0.4rem 0.65rem 0.55rem 0.65rem;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.45);
        margin-bottom: 0.9rem;
    }

    [data-testid="stRadio"] {
        padding: 0.72rem 0.8rem 0.82rem 0.8rem;
    }

    [data-testid="stTextArea"] textarea {
        line-height: 1.65;
    }

    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 16px;
        padding: 0.85rem 1rem;
        font-weight: 800;
        color: white;
        background: linear-gradient(135deg, #1e50d8 0%, #1187b1 100%);
        box-shadow: 0 16px 28px rgba(24, 59, 140, 0.22);
        transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        filter: brightness(1.02);
        box-shadow: 0 20px 32px rgba(24, 59, 140, 0.28);
    }

    [data-testid="stNotification"],
    [data-testid="stAlert"] {
        border-radius: 18px;
    }

    @media (max-width: 980px) {
        .stats-grid,
        .bridge-grid {
            grid-template-columns: 1fr;
        }

        .hero-card {
            padding: 1.4rem;
        }
    }

    @media (max-width: 1200px) {
        .stat-subtle {
            font-size: 0.84rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <section class="hero-card">
        <div class="hero-kicker">AI-Powered Multilingual Pedagogy</div>
        <h1 class="hero-title">Transform monolingual materials into multilingual learning experiences in seconds.</h1>
        <p class="hero-copy">
            Upload a paragraph, article, or PDF and generate a cognitive glossary, a CEFR-adapted bridge text,
            and collaborative classroom activities designed to reduce language load without losing academic rigor.
        </p>
        <div class="hero-badges">
            <span class="hero-badge">Cognitive Glossary</span>
            <span class="hero-badge">B1 Simplification</span>
            <span class="hero-badge">Translanguaging Activities</span>
            <span class="hero-badge">Gemini 2.5 Flash / Pro</span>
        </div>
    </section>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("""
    <div class="sidebar-shell">
        <div class="sidebar-brand">
            <div class="sidebar-kicker">Language Station</div>
            <div class="sidebar-title">Teacher Control Center</div>
            <p class="sidebar-copy">
                Prepare multilingual classroom support in a single flow, with polished outputs built for fast live demonstration.
            </p>
        </div>
        <div class="sidebar-section">Model Selection</div>
    </div>
""", unsafe_allow_html=True)
model_choice = st.sidebar.radio(
    "Select Model Engine:",
    ["Fast Mode (gemini-2.5-flash)", "High Quality (gemini-2.5-pro)"],
    index=0
)

# Map UI selection to actual model names
model_map = {
    "Fast Mode (gemini-2.5-flash)": "gemini-2.5-flash",
    "High Quality (gemini-2.5-pro)": "gemini-2.5-pro"
}
selected_model = model_map[model_choice]

# Initialize session state for the result
if 'result' not in st.session_state:
    st.session_state.result = None

# Load demo text from assets if available
try:
    with open("assets/demo_samples.txt", "r", encoding="utf-8") as f:
        demo_text = f.read()
except Exception:
    demo_text = ""

st.sidebar.markdown("""<div class="sidebar-section">Input Configuration</div>""", unsafe_allow_html=True)
input_mode = st.sidebar.radio("Input Type", ["Use course material", "Describe your lesson"])
language_direction = st.sidebar.radio("Language Support", ["English → Finnish", "Finnish → English"])

st.sidebar.markdown("""
    <div class="sidebar-section" style="margin-top: 1.45rem;">Source Content</div>
""", unsafe_allow_html=True)
uploaded_file = None
input_text = ""

if input_mode == "Use course material":
    uploaded_file = st.sidebar.file_uploader("Upload an academic text or PDF", type=["txt", "pdf"])
    input_text = st.sidebar.text_area(
        "Paste your course material here:",
        height=200,
        value=demo_text,
        placeholder="Paste a paragraph from a lecture, article, or course material..."
    )
else:
    input_text = st.sidebar.text_area(
        "Describe your lesson (topic, students, goals, materials):",
        height=300,
        placeholder="e.g., A lesson about handwashing for first-year nursing students. Focus on hygiene and microbiology terms."
    )

st.sidebar.markdown("### Generate Language Station")
generate_button = st.sidebar.button("Generate Language Station", type="primary")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Main Content Logic
if generate_button:
    source_text = ""
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            source_text = extract_text_from_pdf(uploaded_file)
        else:
            source_text = uploaded_file.read().decode("utf-8")
    elif input_text:
        source_text = input_text
    
    if not source_text.strip():
        st.warning("Please enter or upload an academic text to generate outputs.")
    else:
        # UI Warning for truncation
        if len(source_text) > 15000:
            st.info("Note: The source text is very long. We have truncated it to the most relevant first 15,000 characters for the analysis.")
        
        with st.spinner("Analyzing linguistic complexity and generating multilingual learning resources..."):
            try:
                # Call the LLM engine and store in session state
                st.session_state.result = process_text(
                    source_text, 
                    model_type=selected_model,
                    input_mode=input_mode,
                    language_direction=language_direction
                )
                st.session_state.source_text_cache = source_text # Cache source text too
                st.session_state.lang_dir_cache = language_direction # Cache language direction
            except Exception as e:
                st.error(f"An error occurred during processing: {str(e)}")

# Display Logic (Outside the button click block, triggered by session state)
if st.session_state.result:
    result = st.session_state.result
    source_text = st.session_state.get('source_text_cache', "")
    
    st.markdown("""
        <div class="status-banner">
            Language Station generated successfully. Your multilingual teaching kit is ready for review.
        </div>
    """, unsafe_allow_html=True)

    st.info("This tool transforms monolingual materials into multilingual, translanguaging-based learning experiences.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Key Terms", len(result.glossary))
    col2.metric("Activities", len(result.pedagogy_suggestions))
    col3.metric("Level", "CEFR B1")
    col4.metric("Teacher Time Saved", "Hours to Seconds")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs([
        "Key Academic Terms",
        "Accessible Text",
        "Learning Activities"
    ])
    
    with tab1:
        st.markdown("""
            <div class="section-intro">
                <div class="section-kicker">Academic Language Support</div>
                <h2 class="section-title">Key Academic Terms</h2>
                <p class="section-copy">
                    Verified academic terms with semantic scaffolding, and deterministic Finnish equivalents for high-stakes accuracy.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        for item in result.glossary:
            term = html.escape(item.term)
            translation = html.escape(item.finnish_translation)
            academic_definition = html.escape(item.academic_definition)
            simple_definition = html.escape(item.simple_definition)
            cognitive_note = html.escape(item.cognitive_note)
            
            # Dynamic Labeling based on Mode
            lang_dir = st.session_state.get('lang_dir_cache', "English → Finnish")
            trans_label = "Finnish:" if lang_dir == "English → Finnish" else "English:"
            
            st.markdown(f"""
            <div class="glossary-card">
                <div class="card-meta">
                    <span class="term-chip">Academic Term</span>
                    <span class="translation-chip"><b>{trans_label}</b> <span style="font-size:16px;">{translation}</span></span>
                    <span class="difficulty-chip">High Cognitive Load</span>
                </div>
                <h3 class="term-title">{term}</h3>
                <span class="card-label">Academic Definition</span>
                <p class="card-copy">{academic_definition}</p>
                <span class="card-label">Simplified Meaning</span>
                <p class="card-copy">{simple_definition}</p>
                <div class="cognitive-note">
                    <strong>Why it is difficult:</strong> {cognitive_note}
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
            <div class="section-intro">
                <div class="section-kicker">Before And After</div>
                <h2 class="section-title">Bilingual Bridge</h2>
                <p class="section-copy">
                    Compare the original academic source with a more accessible B1 adaptation while preserving the core teaching content.
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.subheader("Accessible Version for Understanding and Discussion (CEFR B1)")

        display_text = source_text[:15000] + "..." if len(source_text) > 15000 else source_text
        original_text = html.escape(display_text)
        simplified_text = html.escape(result.simplified_text)
        st.markdown(f"""
            <div class="bridge-grid">
                <div class="text-panel original">
                    <div class="panel-label original">Original Source</div>
                    <h3 class="panel-title">Dense academic wording</h3>
                    <p class="panel-copy">{original_text}</p>
                </div>
                <div class="text-panel simplified">
                    <div class="panel-label simplified">CEFR B1 Adaptation</div>
                    <h3 class="panel-title">Clearer language for multilingual learners</h3>
                    <p class="panel-copy">{simplified_text}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
            <div class="section-intro">
                <div class="section-kicker">Teacher-Ready Outputs</div>
                <h2 class="section-title">Pedagogy Planner</h2>
                <p class="section-copy">
                    Text-specific classroom activities designed to support collaboration, translanguaging, and fast lesson preparation.
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("## Lesson Planning: Collaborative Groupwork Activities")
        st.caption("Designed to support lesson planning with ready-to-use teaching methods.")
        st.markdown("### Ready-to-Use Classroom Activities")
        st.caption("Designed for immediate use in multilingual classrooms")
        
        for i, activity in enumerate(result.pedagogy_suggestions, 1):
            activity_name = html.escape(activity.activity_name)
            instructions = html.escape(activity.instructions)
            st.markdown(f"""
            <div class="planner-card">
                <div class="planner-chip">Activity {i}</div>
                <h3 class="planner-title">{activity_name}</h3>
                <p class="planner-copy">{instructions}</p>
            </div>
            """, unsafe_allow_html=True)
        st.caption("Copy and use these directly in your classroom.")
else:
    st.markdown("""
        <div class="empty-state">
            Choose your input mode in the sidebar to either upload academic material or describe a lesson plan.
            Then click <strong>Generate Language Station</strong> to instantly create a cognitive glossary,
            CEFR-adapted text, and ready-to-use pedagogical activities.
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""<div class="footer-note">Developed for Sohjo Hacks | Multilingual Pedagogy Project</div>""", unsafe_allow_html=True)
