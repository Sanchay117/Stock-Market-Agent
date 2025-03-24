from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.langchain_agent import create_agent

app = FastAPI()
agent = create_agent()

class StockQuery(BaseModel):
    ticker: str
    query: str = "What's the current price and should I buy/sell/hold?"

@app.post("/stock-info")
def get_stock_info(stock_query: StockQuery):
    try:
        prompt = f"Ticker: {stock_query.ticker}\nQuery: {stock_query.query}"
        response = agent.run(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
