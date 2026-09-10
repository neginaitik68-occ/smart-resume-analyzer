from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_text_similarity(resume_text, job_description):

    if not resume_text or not job_description:
        return 0

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    similarity_score = similarity[0][0] * 100

    return round(similarity_score, 2)