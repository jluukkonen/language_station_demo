"""
Mockup Database for Language Station (UEF Demo Edition)
Contains realistic student personas and course profiles for the University of Eastern Finland.
"""

MOCK_STUDENTS = [
    {
        "id": "std_1",
        "name": "Aino Korhonen (Nursing, B1)",
        "year": 2,
        "program": "Nursing",
        "completed_courses": ["Anatomy 1", "Basic Chemistry", "Introduction to Healthcare"],
        "cefr": "B1",
        "goal": "Prepare for clinical practice in a Finnish hospital.",
        "avatar": "🩺"
    },
    {
        "id": "std_2",
        "name": "Lauri Virtanen (Nursing, B2)",
        "year": 3,
        "program": "Nursing",
        "completed_courses": ["Microbiology", "Pathophysiology", "Pharmacology"],
        "cefr": "B2",
        "goal": "Write a professional medical report in Finnish.",
        "avatar": "💊"
    },
    {
        "id": "std_3",
        "name": "Elias Mäkelä (Engineering, A2)",
        "year": 1,
        "program": "Sustainable Engineering",
        "completed_courses": ["Mathematics 101"],
        "cefr": "A2",
        "goal": "Understand technical safety manuals for laboratory work.",
        "avatar": "⚙️"
    },
    {
        "id": "std_4",
        "name": "Ina-Maria Silva (Forestry, A1)",
        "year": 1,
        "program": "International Forestry (Master's)",
        "completed_courses": ["Global Forest Policy"],
        "cefr": "A1",
        "goal": "Learn basic Finnish tree species and ecosystem terminology.",
        "avatar": "🌲"
    },
    {
        "id": "std_5",
        "name": "Ahmed Al-Farsi (IT, B2)",
        "year": 4,
        "program": "Computer Science (Exchange)",
        "completed_courses": ["Software Engineering", "AI Ethics", "Data Structures"],
        "cefr": "B2",
        "goal": "Collaborate on a software development project in a Finnish-speaking team.",
        "avatar": "💻"
    },
    {
        "id": "std_6",
        "name": "Viivi Niemi (Education, C1)",
        "year": 5,
        "program": "Primary Education",
        "completed_courses": ["Pedagogy 1-4", "Educational Psychology"],
        "cefr": "C1",
        "goal": "Teach complex scientific concepts to 6th graders in Finnish.",
        "avatar": "🍎"
    }
]

MOCK_COURSES = [
    {
        "name": "--- Select a Lesson Template ---",
        "description": ""
    },
    {
        "name": "Advanced Microbiology 303 (Nursing)",
        "description": "Topic: Mechanisms of bacterial resistance. Goals: Understand common pathogens and antibiotic protocols. Materials: Research paper on MRSA in clinical settings."
    },
    {
        "name": "Silviculture & Ecology (Forestry)",
        "description": "Topic: Boreal forest regeneration. Goals: Identify key Finnish tree species (mänty, kuusi, koivu). Materials: Field guide to Northern European ecosystems."
    },
    {
        "name": "Technical Thermodynamics (Engineering)",
        "description": "Topic: Energy efficiency in industrial cooling. Goals: Explain the second law of thermodynamics. Materials: Technical manual for heat exchangers."
    }
]
