"""
Mockup Database for Language Station (UEF Demo Edition)
Contains realistic student personas and course profiles for the University of Eastern Finland.
"""

MOCK_STUDENTS = [
    {
        "id": "std_1",
        "name": "Student A (Health, B1)",
        "year": 2,
        "program": "Human and Planetary Health",
        "completed_courses": ["Anatomy 1", "Basic Chemistry", "Introduction to Healthcare", "Health Communication"],
        "cefr": "B1",
        "goal": "Prepare for clinical practice in a Finnish hospital.",
        "avatar": "🩺",
        "home_languages": ["Finnish (Native)", "English (B2)"],
        "schooling_language": "Finnish",
        "linguistic_repertoire": ["Finnish", "English", "Swedish (Basics)"],
        "linguistic_barrier": "Passive voice in academic writing"
    },
    {
        "id": "std_2",
        "name": "Student B (Health, B2)",
        "year": 3,
        "program": "Human and Planetary Health",
        "completed_courses": ["Microbiology", "Pathophysiology", "Pharmacology", "Clinical Skills 1"],
        "cefr": "B2",
        "goal": "Write a professional medical report in Finnish.",
        "avatar": "💊",
        "home_languages": ["Finnish (Native)", "Swedish (B1)", "English (B2)"],
        "schooling_language": "Finnish",
        "linguistic_repertoire": ["Finnish", "Swedish", "English", "German (Basics)"],
        "linguistic_barrier": "Highly technical Latinate medical terminology"
    },
    {
        "id": "std_3",
        "name": "Student C (Engineering, A2)",
        "year": 1,
        "program": "Biomedical Engineering",
        "completed_courses": ["Mathematics 101", "Introduction to Engineering", "Physics Fundamentals"],
        "cefr": "A2",
        "goal": "Understand technical safety manuals for laboratory work.",
        "avatar": "⚙️",
        "home_languages": ["Finnish (Native)", "English (A2)"],
        "schooling_language": "Finnish",
        "linguistic_repertoire": ["Finnish", "English"],
        "linguistic_barrier": "Complex prepositional phrases in safety manuals"
    },
    {
        "id": "std_4",
        "name": "Student D (Forestry, A1)",
        "year": 1,
        "program": "International Forestry (Master's)",
        "completed_courses": ["Global Forest Policy", "Introduction to Boreal Forests"],
        "cefr": "A1",
        "goal": "Learn basic Finnish tree species and ecosystem terminology.",
        "avatar": "🌲",
        "home_languages": ["Portuguese (Native)", "Spanish (B2)", "English (B2)", "Finnish (A1)"],
        "schooling_language": "Other than Finnish/Swedish",
        "linguistic_repertoire": ["Portuguese", "Spanish", "English", "Finnish"],
        "linguistic_barrier": "Finnish cases (partitive/genitive) for tree species"
    },
    {
        "id": "std_5",
        "name": "Student E (IT, B2)",
        "year": 4,
        "program": "Computer Science (Exchange)",
        "completed_courses": ["Software Engineering", "AI Ethics", "Data Structures", "Human-Computer Interaction"],
        "cefr": "B2",
        "goal": "Collaborate on a software development project in a Finnish-speaking team.",
        "avatar": "💻",
        "home_languages": ["Arabic (Native)", "English (Fluent)", "Finnish (B1)"],
        "schooling_language": "Other than Finnish/Swedish",
        "linguistic_repertoire": ["Arabic", "English", "Finnish"],
        "linguistic_barrier": "Spoken 'puhekieli' vs written 'yleiskieli' in team meetings"
    },
    {
        "id": "std_6",
        "name": "Student F (Education, C1)",
        "year": 5,
        "program": "Primary Education",
        "completed_courses": ["Pedagogy 1-4", "Educational Psychology", "Curriculum Design", "Assessment in Schools"],
        "cefr": "C1",
        "goal": "Teach complex scientific concepts to 6th graders in Finnish.",
        "avatar": "🍎",
        "home_languages": ["Finnish (Native)", "English (C1)", "German (B1)"],
        "schooling_language": "Finnish",
        "linguistic_repertoire": ["Finnish", "English", "German"],
        "linguistic_barrier": "Simplifying high-level pedagogical theory for younger learners"
    },
    {
        "id": "std_7",
        "name": "Student G (Business, B1)",
        "year": 2,
        "program": "Business School",
        "completed_courses": ["Introduction to Marketing", "Business Mathematics", "Academic English for Business"],
        "cefr": "B1",
        "goal": "Participate confidently in Finnish-speaking group presentations.",
        "avatar": "📊",
        "home_languages": ["Vietnamese (Native)", "English (B2)", "Finnish (B1)"],
        "schooling_language": "Other than Finnish/Swedish",
        "linguistic_repertoire": ["Vietnamese", "English", "Finnish"],
        "linguistic_barrier": "Nominalized academic language in business case texts"
    },
    {
        "id": "std_8",
        "name": "Student H (Social Work, B2)",
        "year": 4,
        "program": "Social Work",
        "completed_courses": ["Introduction to Social Work", "Welfare Systems", "Community Studies", "Research Methods"],
        "cefr": "B2",
        "goal": "Use professional client-interaction language in Finnish and English.",
        "avatar": "🤝",
        "home_languages": ["Finnish (Native)", "English (B2)"],
        "schooling_language": "Finnish",
        "linguistic_repertoire": ["Finnish", "English", "Swedish (Basics)"],
        "linguistic_barrier": "Balancing formal terminology with empathetic client language"
    },
    {
        "id": "std_9",
        "name": "Student I (Environmental Science, B2)",
        "year": 2,
        "program": "Environmental Science",
        "completed_courses": ["Ecology Basics", "Statistics for Natural Sciences", "GIS Foundations"],
        "cefr": "B2",
        "goal": "Discuss environmental data and field observations in Finnish seminars.",
        "avatar": "🌍",
        "home_languages": ["Polish (Native)", "English (C1)", "Finnish (B1)"],
        "schooling_language": "Other than Finnish/Swedish",
        "linguistic_repertoire": ["Polish", "English", "Finnish"],
        "linguistic_barrier": "Dense passive constructions in scientific reports"
    },
    {
        "id": "std_10",
        "name": "Student J (Nursing, A2)",
        "year": 1,
        "program": "Nursing",
        "completed_courses": ["Orientation to Nursing Studies", "Basic Finnish for Healthcare"],
        "cefr": "A2",
        "goal": "Build core healthcare vocabulary for patient interaction.",
        "avatar": "🧼",
        "home_languages": ["Finnish (Native)", "English (A2)"],
        "schooling_language": "Finnish",
        "linguistic_repertoire": ["Finnish", "English"],
        "linguistic_barrier": "Remembering medical terms while processing instructions in real time"
    },
    {
        "id": "std_11",
        "name": "Student K (Education, B1)",
        "year": 3,
        "program": "Early Childhood Education",
        "completed_courses": ["Child Development", "Inclusive Pedagogy", "Classroom Interaction"],
        "cefr": "B1",
        "goal": "Explain child development concepts in accessible Finnish.",
        "avatar": "🧩",
        "home_languages": ["Somali (Native)", "English (B2)", "Finnish (B1)"],
        "schooling_language": "Other than Finnish/Swedish",
        "linguistic_repertoire": ["Somali", "English", "Finnish"],
        "linguistic_barrier": "Abstract developmental terminology in academic articles"
    },
    {
        "id": "std_12",
        "name": "Student L (Forestry, C1)",
        "year": 2,
        "program": "Forest Sciences",
        "completed_courses": ["Forest Ecology", "Silviculture Basics", "Remote Sensing for Forests", "Scientific Writing"],
        "cefr": "C1",
        "goal": "Lead technical field discussions and write concise bilingual summaries.",
        "avatar": "🪵",
        "home_languages": ["Swedish (Native)", "Finnish (C1)", "English (C1)"],
        "schooling_language": "Swedish",
        "linguistic_repertoire": ["Swedish", "Finnish", "English"],
        "linguistic_barrier": "Switching between field jargon and student-friendly explanations"
    }
]

MOCK_COURSES = [
    {
        "name": "--- Select a Lesson Template ---",
        "description": ""
    },
    {
        "name": "TL00EY06 Microbiology in Health Sciences (4 ECTS)",
        "description": "Topic: Mechanisms of bacterial resistance (MRSA). Goals: Understand pathogens and antibiotic protocols. Translanguaging Goal: integrate Finnish clinical vocabulary with English research."
    },
    {
        "name": "TL00EY11 Public and Planetary Health (2 ECTS)",
        "description": "Topic: Environmental health. Translanguaging Goal: compare health policies across languages."
    },
    {
        "name": "S2-Integration: Biomedical Laboratory Practice",
        "description": "Topic: Lab safety. Goal: learn Finnish safety language during engineering tasks."
    },
    {
        "name": "Nursing Communication Lab: Patient Instructions",
        "description": "Topic: Clear patient guidance in ward settings. Goals: practice plain Finnish, key clinical vocabulary, and bilingual explanation strategies for patient safety."
    },
    {
        "name": "Forest Ecology Fieldwork and Species Identification",
        "description": "Topic: Boreal forest ecosystems and tree species. Goals: connect field observations with Finnish and English scientific terminology and short oral explanations."
    },
    {
        "name": "Computer Science Team Sprint: AI Ethics in Practice",
        "description": "Topic: Ethical trade-offs in software development. Goals: discuss cases in mixed-language teams and produce concise Finnish-English project communication."
    },
    {
        "name": "Education Seminar: Explaining Science to Young Learners",
        "description": "Topic: Age-appropriate science teaching. Goals: simplify academic content, design multimodal classroom activities, and connect pedagogical theory to accessible language."
    },
    {
        "name": "Social Work Case Discussion: Client Meetings",
        "description": "Topic: Welfare services and client communication. Goals: balance professional terminology with empathetic language in Finnish and English group tasks."
    },
    {
        "name": "Business Case Workshop: Sustainable Product Launch",
        "description": "Topic: Marketing and stakeholder communication. Goals: interpret business case materials, discuss strategy in multilingual teams, and practice presentation language."
    },
    {
        "name": "Environmental Science Data Lab: Water Quality",
        "description": "Topic: Reading graphs, field data, and environmental indicators. Goals: describe evidence clearly, compare findings across languages, and use discipline-specific vocabulary accurately."
    }
]
