from data_collector import collect_market_data
from llm_client import analyze_with_llm

async def generate_report(sector: str) -> str:
    market_data = await collect_market_data(sector)

    if not market_data:
        market_data = [
            f"No major breaking news found, but the {sector} sector shows ongoing activity."
        ]

    return await analyze_with_llm(sector, market_data)
