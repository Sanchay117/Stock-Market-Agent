from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

import yfinance as yf

def get_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.info.get("regularMarketPrice", "Price not found")
    return price

print(get_price("AAPL"))

# def get_price_from_yahoo(url):
#     response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#     soup = BeautifulSoup(response.text, 'html.parser')
#     price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
#     if price_tag:
#         return price_tag.text
#     return "Price not found"
#
# # Example:
# yahoo_url = "https://finance.yahoo.com/quote/AAPL"
# price = get_price_from_yahoo(yahoo_url)
# print("Current price:", price)
#
# def search_stock_info(ticker, num_results=5):
#     query = f"{ticker} stock price site:yahoo.com OR site:marketwatch.com OR site:bloomberg.com"
#     with DDGS() as ddgs:
#         results = ddgs.text(query, region='wt-wt', safesearch='off', max_results=num_results)
#         for result in results:
#             print(f"Title: {result['title']}")
#             print(f"Link: {result['href']}")
#             print(f"Body: {result['body']}")
#             print('---')
#
#
# search_stock_info("AAPL")
