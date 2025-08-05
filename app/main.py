from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.services.openai_service import analyze_metrics_with_openai


app = FastAPI()

class AnalyzeRequest(BaseModel):
    metrics: dict
    question: str


@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    result = analyze_metrics_with_openai(request.metrics, request.question)
    return {"answer": result}