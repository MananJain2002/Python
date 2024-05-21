from telegram import Bot
from dotenv import load_dotenv
import requests, asyncio, os

load_dotenv()

# Load API key and location coordinates from environment variables
API_KEY = os.getenv("API_KEY")
LATITUDE = 17.385044
LONGITUDE = 78.486671

# Set weather parameters for API request
weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "cnt": 4,
    "appid": API_KEY
}

# Define an asynchronous function to send rain alert
async def send_alert():
    # Create a Telegram bot instance using the bot token from environment variable
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    # Get the chat ID from environment variable
    chat_id = os.getenv("CHAT_ID")

    # Send a GET request to OpenWeatherMap API to fetch weather forecast
    with requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params) as response:
        response.raise_for_status()
        # Extract the weather data from the response
        weather_data = response.json()['list']
        # Iterate through each hour's weather data
        for hour_data in weather_data:
            # Check if the weather condition code is less than 700 (indicating rain)
            if int(hour_data['weather'][0]['id']) < 700:
                # Send a message to the specified chat ID indicating rain
                await bot.send_message(chat_id=chat_id, text="It's going to rain today. Remember to bring an ☔")
                break

# Run the send_alert function asynchronously
asyncio.run(send_alert())