# AI Resume–Job Match Scoring API

## Overview
A Dockerized NLP-based REST API that calculates resume-to-job
match scores using TF-IDF and cosine similarity.

## Tech Stack
- Python
- FastAPI
- NLP (TF-IDF)
- Docker

## Endpoints
- GET /health
- POST /match

## Run Locally
uvicorn app.main:app --reload

## Run with Docker
docker build -t ai-resume-match-api .
docker run -p 8000:8000 ai-resume-match-api
