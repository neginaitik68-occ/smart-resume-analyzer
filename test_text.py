from utils.text_processing import clean_text


sample_text = """
I am a Python Developer with 2 years of experience.
I have worked with Pandas, SQL, and Machine Learning!
"""

cleaned = clean_text(sample_text)

print("Original Text:")
print(sample_text)

print("\nCleaned Text:")
print(cleaned)