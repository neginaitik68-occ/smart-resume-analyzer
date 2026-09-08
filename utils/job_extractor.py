from utils.resume_extractor import SKILLS


def extract_job_skills(job_description):

    job_description = job_description.lower()

    required_skills = []

    for skill in SKILLS:

        if skill in job_description:
            required_skills.append(skill)

    return required_skills