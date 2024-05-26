from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os, asyncio, smtplib

load_dotenv()

SHEETY_PASSWORD = os.getenv("PASSWORD")
SHEETY_KEY = os.getenv("SHEETY_KEY")

TEQUILA_API = os.getenv("TEQUILA_API")

TELEGRAM_API = os.getenv("TELEGRAM_API")
CHAT_ID = os.getenv("CHAT_ID")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

ORIGIN_CITY_IATA = "LON"

def update_missing_iata_codes():
    missing_cities = dataManager.missing_iata_codes()
    for city in missing_cities:
        city_code = flightSearch.get_iata_codes(city["city"])
        dataManager.update_iata_codes(city_code, city["id"])
    
async def compare_price(users):
    """
    Compare flight prices with the lowest prices stored in the sheet_data.
    If a flight price is lower than the lowest price, send a notification email to the user.

    Args:
        users (list): A list of user dictionaries containing email addresses.

    Returns:
        None
    """

    tasks = []  # List to store the notification tasks
    messages = ""  # String to store the notification messages

    for data in sheet_data:
        # Get the best price for the flight
        flight = flightSearch.get_best_price(ORIGIN_CITY_IATA, data["iataCode"], date_from, date_to)

        if not flight:
            continue

        if flight.price < int(data["lowestPrice"]):
            # Create the notification message
            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            messages += f"\n{message}"  # Add the message to the messages string

            # Create a task to send the notification message
            task = asyncio.create_task(notificationManager.send_message(message))
            tasks.append(task)

    for user in users:
        email = user["email"]

        # Connect to the SMTP server and send the notification email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Flight Price!\n\n{messages}".encode('utf-8')
            )

    await asyncio.gather(*tasks)  # Wait for all tasks to complete

dataManager = DataManager(SHEETY_PASSWORD, SHEETY_KEY)
flightSearch = FlightSearch(TEQUILA_API)
notificationManager = NotificationManager(TELEGRAM_API, CHAT_ID)

update_missing_iata_codes()
sheet_data = dataManager.sheet_data

date_from = datetime.now().date().strftime("%d/%m/%Y")
date_to = (datetime.now() + relativedelta(months=+6)).date().strftime("%d/%m/%Y")

if input("Do you want to add a new user? Type y to add a new user: ").lower() == "y":
    dataManager.create_user()

users = dataManager.get_user()

asyncio.run(compare_price(users))