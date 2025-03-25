from fastapi import FastAPI, HTTPException, Query
from stock_fetcher import get_info

app = FastAPI()

@app.get("/")
def root():
    return {
        "Home": "Welcome to the AI Stock Market Agent! 🚀",
        "Instructions": "POST to /ticker with a 'name' query parameter to get stock data and recent news."
    }

@app.get("/ticker")
def ticker(name: str = Query(..., description="Ticker symbol, e.g., AAPL, TSLA")):
    result = get_info(name)
    if result == -1:
        raise HTTPException(status_code=404, detail=f"Stock {name} not found or data unavailable")
    else:
        return result
