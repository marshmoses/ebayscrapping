
from fastapi import FastAPI
from typing import Optional
import requests

app = FastAPI()

# Define eBay API endpoint
EBAY_API_URL = "https://api.ebay.com/buy/browse/v1/item_summary/search"

# Replace 'YOUR_OAUTH_TOKEN' with your actual OAuth token
OAUTH_TOKEN = "v^1.1#i^1#r^1#f^0#I^3#p^3#t^Ul4xMF8xMTo2Q0IxMkU1NkFFNDdBMERBMjNBNDU1OUYwN0Q1QzU3Nl8wXzEjRV4yNjA="

# Define function to fetch eBay data
def fetch_ebay_data(query: str, limit: int = 10):
    headers = {
        "Authorization": f"Bearer {OAUTH_TOKEN}",
        "Accept": "application/json"
    }
    params = {
        "q": query,
        "limit": limit
    }
    response = requests.get(EBAY_API_URL, headers=headers, params=params)
    data = response.json()
    return data

# Define FastAPI endpoint to fetch eBay data
@app.get("/ebay/")
def get_ebay_data(query: str, limit: Optional[int] = 10):
    ebay_data = fetch_ebay_data(query, limit)
    return ebay_data
