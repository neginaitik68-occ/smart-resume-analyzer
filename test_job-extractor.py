from utils.job_extractor import extract_job_skills


job_description = """
We are looking for a Data Scientist.

Required skills:
Python
Pandas
SQL
Machine Learning
Power BI

Experience with Git and Docker is a plus.
"""


skills = extract_job_skills(job_description)


print("Required Job Skills:")
print(skills)