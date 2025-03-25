from langchain_community.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from langchain.agents import initialize_agent
from stock_fetcher import get_info
import os

# Initialize Hugging Face model (Replace with your Hugging Face API key)
HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACE_API_TOKEN")

llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-alpha",   # You can replace this with any conversational Hugging Face model
    model_kwargs={"temperature": 0.7, "max_length": 1024},
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
)

# Define a custom tool to fetch stock data
def fetch_stock_data(ticker: str):
    info = get_info(ticker)
    if info == -1:
        return f"Could not find stock information for {ticker}."

    price = info.get("Current Price")
    title = info.get("Latest News Title", "No recent headline available.")
    body = info.get("Latest News Body", "No summary available.")

    return f"Stock: {ticker}\nPrice: {price}\nRecent Headline: {title}\nSummary: {body}"


# Define LangChain tool
stock_tool = Tool(
    name="Stock Info Fetcher",
    func=fetch_stock_data,
    description="Fetches real-time stock price and latest market news for a given ticker."
)

# Custom prompt template for recommendation
prompt_template = PromptTemplate(
    input_variables=["stock_data"],
    template="""
You are an AI financial advisor. Based on the following stock information:

{stock_data}

Analyze the stock price and recent market news, then give a recommendation on whether to BUY, SELL, or HOLD.
Explain your reasoning in 2-3 lines.
"""
)

# Agent setup
agent = initialize_agent(
    tools=[stock_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Function to get stock recommendation (with prompt removal)
def get_stock_recommendation(ticker: str):
    stock_data = fetch_stock_data(ticker)
    prompt = prompt_template.format(stock_data=stock_data)
    response = llm.invoke(prompt)

    if isinstance(response, dict):
        text = response.get("generated_text", "")
    else:
        text = response

    # Remove prompt from the output if present
    cleaned_text = text.replace(prompt, "").replace("Possible response:", "").strip()

    return cleaned_text
