def calculate_skill_match(resume_skills, job_skills):

    if not job_skills:
        return 0

    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    matched_skills = resume_skills.intersection(job_skills)

    match_percentage = (
        len(matched_skills) / len(job_skills)
    ) * 100

    return round(match_percentage, 2)


def get_matched_skills(resume_skills, job_skills):

    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    return sorted(resume_skills.intersection(job_skills))


def get_missing_skills(resume_skills, job_skills):

    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    return sorted(job_skills - resume_skills)