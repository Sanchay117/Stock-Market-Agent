from duckduckgo_search import DDGS

def get_info(ticker: str, num_results: int = 1):
    try:
        query = f"{ticker} stock price site:yahoo.com OR site:marketwatch.com OR site:bloomberg.com"
        info = {}

        with DDGS() as ddgs:
            results = ddgs.text(query, region='wt-wt', safesearch='off', max_results=num_results)
            for result in results:
                info["Title"] = result['title']
                info["Link"] = result['href']
                info["Body"] = result['body']

                # Attempt to extract price if present in the body or title
                price = extract_price_from_text(result['body']) or extract_price_from_text(result['title'])
                if price:
                    info["Price"] = price
                else:
                    info["Price"] = "Not found in snippet"
                break  # Only first result

        if not info:
            return -1

        return info

    except Exception as e:
        print(f"Error while fetching info for {ticker}: {e}")
        return -1


def extract_price_from_text(text: str):
    import re
    # Regex to find something that looks like a price (e.g., $123.45 or USD 123.45)
    match = re.search(r'(\$|USD\s?)\s?([0-9]+(\.[0-9]{1,2})?)', text)
    if match:
        return match.group(0)
    return None
