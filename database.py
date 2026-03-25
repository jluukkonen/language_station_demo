"""
Mockup Database for Language Station (UEF Demo Edition)
Contains realistic student personas and course profiles for the University of Eastern Finland.
"""

MOCK_STUDENTS = [
    {
        "id": "std_1",
        "name": "Aino Korhonen (Health, B1)",
        "year": 2,
        "program": "Human and Planetary Health",
        "completed_courses": ["Anatomy 1", "Basic Chemistry", "Introduction to Healthcare"],
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
        "name": "Lauri Virtanen (Health, B2)",
        "year": 3,
        "program": "Human and Planetary Health",
        "completed_courses": ["Microbiology", "Pathophysiology", "Pharmacology"],
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
        "name": "Elias Mäkelä (Engineering, A2)",
        "year": 1,
        "program": "Biomedical Engineering",
        "completed_courses": ["Mathematics 101"],
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
        "name": "Ina-Maria Silva (Forestry, A1)",
        "year": 1,
        "program": "International Forestry (Master's)",
        "completed_courses": ["Global Forest Policy"],
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
        "name": "Ahmed Al-Farsi (IT, B2)",
        "year": 4,
        "program": "Computer Science (Exchange)",
        "completed_courses": ["Software Engineering", "AI Ethics", "Data Structures"],
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
        "name": "Viivi Niemi (Education, C1)",
        "year": 5,
        "program": "Primary Education",
        "completed_courses": ["Pedagogy 1-4", "Educational Psychology"],
        "cefr": "C1",
        "goal": "Teach complex scientific concepts to 6th graders in Finnish.",
        "avatar": "🍎",
        "home_languages": ["Finnish (Native)", "English (C1)", "German (B1)"],
        "schooling_language": "Finnish",
        "linguistic_repertoire": ["Finnish", "English", "German"],
        "linguistic_barrier": "Simplifying high-level pedagogical theory for younger learners"
    }
],

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
    }
]
