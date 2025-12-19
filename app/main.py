from fastapi import FastAPI
from app.schema import MatchRequest
from app.model import calculate_match

app = FastAPI(title="AI Resume Match API")

@app.get("/health")
def health():
    return {"status": "API is running"}

@app.post("/match")
def match_resume(data: MatchRequest):
    score, missing = calculate_match(
        data.resume_text,
        data.job_text
    )

    return {
        "match_score": score,
        "missing_skills": missing
    }

