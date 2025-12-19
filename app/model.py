from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

sample_texts = [
    "python sql machine learning pandas numpy",
    "java spring boot microservices",
    "python fastapi docker sql",
    "data analysis python pandas matplotlib",
    "machine learning deep learning python"
]

vectorizer = TfidfVectorizer(stop_words="english")
vectorizer.fit(sample_texts)

joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")
print("TF-IDF vectorizer saved.")
