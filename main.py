import requests
from access import *

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = jt_stock_api

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = jt_news_api

# getting yesterdays closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# getting the day before yesterday's closing stock price 
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
 
# find the positive difference between the closing stock price on the previous two days
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

# percentage difference between the closing price yesterday and day before 
diff_percent = (difference / float(yesterday_closing_price)) * 100
print (diff_percent)

# if the percent difference is greater than 5, Get News articles using NewsAPI
if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)














