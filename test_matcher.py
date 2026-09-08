from utils.matcher import (
    calculate_skill_match,
    get_matched_skills,
    get_missing_skills
)


resume_skills = [
    "python",
    "pandas",
    "sql",
    "git"
]


job_skills = [
    "python",
    "pandas",
    "sql",
    "machine learning",
    "power bi"
]


score = calculate_skill_match(
    resume_skills,
    job_skills
)

matched = get_matched_skills(
    resume_skills,
    job_skills
)

missing = get_missing_skills(
    resume_skills,
    job_skills
)


print("Match Score:", score, "%")
print("Matched Skills:", matched)
print("Missing Skills:", missing)