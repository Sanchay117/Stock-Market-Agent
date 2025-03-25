from duckduckgo_search import DDGS

def fetch_stock_price(ticker: str) -> str:
    query = f"current price of {ticker} stock"
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        if not results:
            return "Could not fetch price."
        # Attempt to parse price from snippet text
        for result in results:
            if "USD" in result['body'] or "$" in result['body']:
                return result['body']
        return "Price information not found."
