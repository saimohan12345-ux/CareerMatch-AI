import json
import re


def load_skills():

    with open("data/skills.json", "r") as file:
        return json.load(file)


def extract_skills(text):

    skills_data = load_skills()

    text = text.lower()

    found_skills = []

    for category, skills in skills_data.items():

        for skill in skills:

            skill_lower = skill.lower()

            # Allow flexible spaces and hyphens
            pattern_text = re.escape(skill_lower)

            pattern_text = pattern_text.replace(
                r"\ ",
                r"[\s\-]+"
            )

            pattern = r"\b" + pattern_text + r"\b"

            if re.search(pattern, text):

                found_skills.append(skill_lower)

    return sorted(set(found_skills))


# --------------------------------------------------
# Skill aliases
# --------------------------------------------------

ALIASES = {

    # REST APIs
    "restful api": "rest api",
    "restful apis": "rest api",
    "rest apis": "rest api",
    "rest api": "rest api",

    # Databases
    "postgres": "postgresql",
    "postgres sql": "postgresql",
    "postgresql": "postgresql",

    # Object Oriented Programming
    "object oriented programming": "oop",
    "object-oriented programming": "oop",
    "oops": "oop",
    "oop": "oop",

    # AI
    "artificial intelligence": "ai",
    "ai": "ai",

    # Machine Learning
    "machine learning": "machine learning",
    "ml": "machine learning",

    # Deep Learning
    "deep learning": "deep learning",
    "dl": "deep learning",

    # Software Development Life Cycle
    "software development life cycle": "sdlc",
    "software development lifecycle": "sdlc",
    "sdlc": "sdlc"
}


def normalize_skills(skills):

    normalized = []

    for skill in skills:

        skill = skill.lower().strip()

        # Convert aliases to canonical names
        skill = ALIASES.get(skill, skill)

        normalized.append(skill)

    return sorted(set(normalized))