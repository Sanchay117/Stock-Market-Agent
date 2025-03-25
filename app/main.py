from fastapi import FastAPI, HTTPException, Query
from stock_fetcher import get_info
app = FastAPI()

@app.get("/")
def root():
    return {"Home": "Hi! Welcome To my AI Stock Market Agent, to..."}

@app.post("/ticker")
def ticker(name: str = Query(..., description="Ticker symbol, e.g., AAPL, TSLA")):
    result = get_info(name)
    if result == -1:
        raise HTTPException(status_code=404, detail=f"Stock {name} not found")
    else:
        return result
