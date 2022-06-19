import requests
from access import *

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = jt_stock_api

# getting yesterdays closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey":stock_api_key
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json)






















