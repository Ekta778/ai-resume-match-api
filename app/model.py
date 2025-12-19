import joblib
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

def clean_text(text: str):
    return text.lower()

def calculate_match(resume_text: str, job_text: str):
    resume_text = clean_text(resume_text)
    job_text = clean_text(job_text)

    vectors = vectorizer.transform([resume_text, job_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    resume_words = set(resume_text.split())
    job_words = set(job_text.split())
    missing_skills = list(job_words - resume_words)

    return round(similarity * 100, 2), missing_skills
