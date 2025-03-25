import os
import finnhub
from duckduckgo_search import DDGS

finnhub_client = finnhub.Client(api_key=os.environ.get("FINNHUB_API_KEY"))

def get_info(ticker: str, num_results: int = 1):
    try:
        ticker = ticker.upper()

        # Get price details
        quote = finnhub_client.quote(ticker)
        if quote['c'] == 0:
            return -1

        # Get company profile
        profile = finnhub_client.company_profile2(symbol=ticker)

        # Get financial metrics
        metrics = finnhub_client.company_basic_financials(ticker, 'all').get('metric', {})

        info = {
            "Ticker": ticker,
            "Company Name": profile.get('name'),
            "Exchange": profile.get('exchange'),
            "Industry": profile.get('finnhubIndustry'),
            "Logo": profile.get('logo'),
            "Current Price": quote['c'],
            "High (Today)": quote['h'],
            "Low (Today)": quote['l'],
            "Open (Today)": quote['o'],
            "Previous Close": quote['pc'],
            "Market Cap": metrics.get('marketCapitalization'),
            "P/E Ratio": metrics.get('peNormalizedAnnual'),
            "Dividend Yield": metrics.get('dividendYieldIndicatedAnnual'),
            "52-Week High": metrics.get('52WeekHigh'),
            "52-Week Low": metrics.get('52WeekLow')
        }

        # Add DuckDuckGo news snippet
        query = f"{ticker} stock site:marketwatch.com OR site:yahoo.com OR site:bloomberg.com"
        with DDGS() as ddgs:
            results = ddgs.text(query, region='wt-wt', safesearch='off', max_results=num_results)
            for result in results:
                info["Latest News Title"] = result['title']
                info["Latest News Body"] = result['body']
                info["Latest News Link"] = result['href']
                break

        return info

    except Exception as e:
        print(f"Error while fetching info for {ticker}: {e}")
        return -1
