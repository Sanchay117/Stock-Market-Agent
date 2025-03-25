# AI Stock Market Agent

A FastAPI-based stock market assistant that fetches real-time stock information, the latest market news, and provides AI-powered buy/sell/hold recommendations.

## Features

- Fetches the latest stock market prices for the requested ticker/stock using the Finnhub API.
- Provides AI-based stock recommendations using LangChain and various LLM models through the HuggingFace API.
- RESTful API endpoints to fetch data and AI analysis.
- Integrates with DuckDuckGo for the latest news.

## Project Structure

```
app/
   ├── main.py               # FastAPI server
   ├── stock_fetcher.py      # Fetches real-time stock info and news
   ├── langchain_agent.py    # Integrates with LangChain and Hugging Face for AI recommendations
├── requirements.txt      # Python dependencies
```

## Limitations

The project can only list US based stocks right now as the free tier of the finnhub(API I am using) doesn't support other stocks.

Also YahooFinance was only allowing me like 5 queries an hour making development extremely difficult because of which I had to go with the Finnhub API. 

## ✅ Deployed
The project is live!

Home: https://web-production-d0984.up.railway.app/

Example endpoint: https://web-production-d0984.up.railway.app/ticker?name=TSLA

## Setup Locally

1. Clone the repository

   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>/app
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables

   Create a `.env` file in the project root:

   ```
   FINNHUB_API_KEY=your_finnhub_api_key_here
   HUGGINGFACE_API_TOKEN=your_huggingface_api_token_here
   ```

   Alternatively, export them directly in the shell:

   ```bash
   export FINNHUB_API_KEY=your_finnhub_api_key_here
   export HUGGINGFACE_API_TOKEN=your_huggingface_api_token_here
   ```

5. Run the server

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### GET /

**Description:** Home route with instructions

**Example response:**

```json
{
  "Home": "Welcome to the AI Stock Market Agent! 🚀",
  "Instructions": "POST to /ticker with a 'name' query parameter to get stock data and recent news."
}
```

### GET /ticker?name=TSLA

**Description:** Fetch stock details, latest news, and AI recommendation for the provided ticker.

**Query Parameter:** `name` (Ticker symbol, e.g., AAPL, TSLA)

**Example response:**

```json
{
  "Ticker": "TSLA",
  "Company Name": "Tesla, Inc.",
  "Exchange": "NASDAQ",
  "Industry": "Automobiles",
  "Current Price": 675.50,
  "High (Today)": 685.30,
  "Low (Today)": 670.20,
  "Open (Today)": 673.50,
  "Previous Close": 672.00,
  "Market Cap": 650000000000,
  "P/E Ratio": 98.3,
  "Dividend Yield": 0.0,
  "52-Week High": 900.40,
  "52-Week Low": 580.30,
  "Latest News Title": "Tesla announces new battery technology",
  "Latest News Body": "Tesla unveiled plans for next-gen battery technology during its annual event...",
  "Latest News Link": "https://marketwatch.com/some-news-link",
  "AI analysis": "Recommendation: HOLD. While Tesla's current price is near its weekly average and recent news is positive, the stock shows signs of stabilization."
}
```

## License

MIT License
