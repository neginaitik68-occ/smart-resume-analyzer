from utils.similarity import calculate_text_similarity


resume_text = """
I am a Data Science student with experience in Python,
Pandas, SQL and Machine Learning.
"""


job_description = """
We are looking for a Data Scientist with experience in
Python, Pandas, SQL, Machine Learning and Power BI.
"""


score = calculate_text_similarity(
    resume_text,
    job_description
)


print("Text Similarity Score:", score, "%")