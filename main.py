from multiprocessing.connection import Client
from unittest.util import three_way_cmp
import requests
from access import *

STOCK_NAME = "MSFT"
COMPANY_NAME = "Microsoft Corporation"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = jt_news_api
STOCK_API_KEY = jt_stock_api
TWILIO_SID = jt_twilio_sid
TWILIO_AUTH_TOKEN = jt_twilio_auth

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
if diff_percent > 2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]



# using slice operator that creates a list that contains the first 3 articles 
three_articles = articles[:3]


# creating a list of the first 3 article's headlines and descriptions using list comprehension
formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
print(formatted_articles)


# sending each article as a separate message via Twilio
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.message.create(
        body=article,
        from_="+18596517102",
        to="+13143983570"
    )






