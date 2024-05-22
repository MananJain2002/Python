from dotenv import load_dotenv
from datetime import datetime, timedelta
from telegram import Bot
import requests, os, asyncio

load_dotenv()

# Load environment variables
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Create Telegram bot instance
bot = Bot(TELEGRAM_TOKEN)

# Function to get the most recent trading day
def get_most_recent_trading_day(data, current_day):
    d = 0
    while data["Time Series (Daily)"].get(str(current_day - timedelta(days=d))) is None:
        d += 1
    return str(current_day - timedelta(days=d))

# API URL and parameter
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

# Get current date
now = datetime.now().date()

# Get stock data
with requests.get(url=stock_url, params=stock_params) as stock_response:
    data = stock_response.json()

    # Get the most recent trading days
    yesterday = get_most_recent_trading_day(data, now - timedelta(days=1))
    day_before_yesterday = get_most_recent_trading_day(data, now - timedelta(days=2))

    # Get the closing prices
    yesterday_close = float(data["Time Series (Daily)"][yesterday]['4. close'])
    day_before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday]['4. close'])

    # Calculate percentage change
    percentage_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100

    # Check if percentage change is greater than or equal to 5%
    if abs(percentage_change) >= 5:
        
        # API URL and parameter
        news_url = "https://newsapi.org/v2/everything"
        news_params = {
            "q": COMPANY_NAME,
            "from": yesterday,
            "sortBy": "publishedAt",
            "apiKey": NEWS_API_KEY
        }

        # Send message asynchronously
        async def send_message_async():
            with requests.get(url=news_url, params=news_params) as news_response:
                news = news_response.json()['articles']
                message = f"TSLA: {'🔺' if yesterday_close > day_before_yesterday_close else '🔻'} {round(percentage_change, 2)}%"
                for i in range(3):
                    news_title = news[i]['title']
                    news_description = news[i]['description']
                    if yesterday_close > day_before_yesterday_close:
                        message += f"\nHeadline: {news_title}\n\nBrief: {news_description}"
                        message += "\n\n------------------------------------\n"
                await bot.send_message(chat_id=CHAT_ID, text=message)

        asyncio.run(send_message_async())
