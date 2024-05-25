from dotenv import load_dotenv
from datetime import datetime
import requests, os

load_dotenv()

# Load environment variables from .env file
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETS_USERNAME = os.getenv("USER")
SHEETS_PASSWORD = os.getenv("PSWD")
SHEETS_KEY = os.getenv("SHEETS_KEY")

# API endpoints and project details
SHEETS_URL = "https://api.sheety.co"
SHEETS_PROJECT_NAME = "workoutsTracking"
SHEET_NAME = "workouts"

# Get exercises input from user
exercies = input("Tell me which exercises you did: ")

# API endpoint for natural language exercise tracking
url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Headers for API request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Parameters for API request
params = {
    "query": exercies
}

# Send POST request to track exercises
with requests.post(url=url, headers=headers, json=params) as response:
    response.raise_for_status()
    json = response.json()["exercises"]

# Get current date and time
now = datetime.now()
date = now.date().strftime("%d/%m/%Y")
time = now.time().strftime('%H:%M:%S')

# Headers for Sheets API request
sheets_headers = {
    "Username": SHEETS_USERNAME,
    "Password": SHEETS_PASSWORD
}

# Iterate over exercises and send data to Sheets API
for exercise in json:
    sheets_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    with requests.post(url=f"{SHEETS_URL}/{SHEETS_KEY}/{SHEETS_PROJECT_NAME}/{SHEET_NAME}", headers=headers, json=sheets_params) as response:
        response.raise_for_status()
