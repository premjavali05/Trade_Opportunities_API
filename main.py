from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse
from analyzer import generate_report
from auth import verify_token
from rate_limiter import check_rate_limit

app = FastAPI(
    title="Trade Opportunities API",
    description="Analyzes Indian market sectors and returns AI-generated trade reports",
    version="1.0.0"
)

@app.get("/analyze/{sector}", response_class=PlainTextResponse)
async def analyze_sector(
    sector: str,
    request: Request,
    user: str = Depends(verify_token)
):
    # Rate limiting per user
    if not check_rate_limit(user):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    report = await generate_report(sector)
    return report
