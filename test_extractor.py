from utils.resume_extractor import extract_resume_info


sample_resume = """
Naitik Negi
Data Science Student

Email: naitik@example.com
Phone: 9876543210

Skills:
Python, Pandas, SQL, Machine Learning
"""


resume_info = extract_resume_info(sample_resume)

print("Resume Information:")
print(resume_info)