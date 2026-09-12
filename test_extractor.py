from utils.resume_extractor import extract_resume_info


sample_resume = """
Naitik Negi
Data Science Student

Email: naitik@example.com
Phone: 9876543210

Skills:
Python
PANDAS
SQL
Machine Learning
Data Science
POWER BI
C++
Git
Docker
"""


resume_info = extract_resume_info(sample_resume)


print("Resume Information:")
print(resume_info)


print("\nSkill Categories:")

for category, skills in resume_info["skill_categories"].items():

    print(category, ":", skills)