from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from app.stock_fetcher import fetch_stock_price
from app.config import OPENAI_API_KEY

def create_agent():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)

    def get_price_tool_func(ticker: str):
        return fetch_stock_price(ticker)

    tools = [
        Tool(
            name="StockPriceFetcher",
            func=get_price_tool_func,
            description="Fetches current price of a given stock ticker."
        )
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent="chat-zero-shot-react-description",
        verbose=True
    )
    return agent
