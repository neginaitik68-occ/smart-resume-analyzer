import re


SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "pandas",
    "numpy",
    "matplotlib",
    "machine learning",
    "deep learning",
    "data science",
    "tensorflow",
    "pytorch",
    "flask",
    "django",
    "power bi",
    "excel",
    "git",
    "github",
    "docker"
]


SKILL_CATEGORIES = {
    "Programming": [
        "python",
        "java",
        "c++"
    ],

    "Data Science": [
        "pandas",
        "numpy",
        "matplotlib",
        "machine learning",
        "deep learning",
        "data science",
        "tensorflow",
        "pytorch"
    ],

    "Web Development": [
        "flask",
        "django"
    ],

    "Database": [
        "sql"
    ],

    "Tools": [
        "git",
        "github",
        "docker"
    ],

    "Business & Analytics": [
        "power bi",
        "excel"
    ]
}


def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):

    pattern = r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_name(text):

    lines = text.strip().split("\n")

    for line in lines:

        line = line.strip()

        if line and len(line.split()) <= 4:

            if not any(char.isdigit() for char in line):

                return line

    return None


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        escaped_skill = re.escape(skill)

        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills


def categorize_skills(skills):

    categorized_skills = {}

    for category, category_skills in SKILL_CATEGORIES.items():

        matched = []

        for skill in skills:

            if skill in category_skills:

                matched.append(skill)

        if matched:

            categorized_skills[category] = matched

    return categorized_skills


def extract_resume_info(text):

    skills = extract_skills(text)

    resume_info = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": skills,
        "skill_categories": categorize_skills(skills)
    }

    return resume_info