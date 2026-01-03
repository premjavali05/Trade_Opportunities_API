import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

async def collect_market_data(sector: str) -> list:
    if not SERPAPI_KEY:
        return []

    query = f"{sector} sector India market news"

    # params = {
    #     "engine": "duckduckgo",
    #     "q": query,
    #     "api_key": SERPAPI_KEY,
    #     "kl": "in-en"
    # }

    params = {
        "engine": "google_news",
        "q": f"{sector} India",
        "api_key": SERPAPI_KEY,
        "hl": "en",
        "gl": "in"
    }

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(
            "https://serpapi.com/search.json",
            params=params
        )

    data = response.json()
    results = []

    for item in data.get("organic_results", [])[:6]:
        title = item.get("title")
        snippet = item.get("snippet")
        if title and snippet:
            results.append(f"{title}: {snippet}")

    return results
