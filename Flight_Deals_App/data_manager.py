
import requests

SHEETY_URL = "https://api.sheety.co"
SHEETY_PROJECT_NAME = "flightDeals"
PRICE_SHEET_NAME = "prices"
USERS_SHEET_NAME = "users"

class DataManager:

    class DataManager:
        def __init__(self, sheety_password, sheety_key):
            """
            Initializes a new instance of the DataManager class.

            Args:
                sheety_password (str): The password for accessing the Sheety API.
                sheety_key (str): The API key for accessing the Sheety API.

            Attributes:
                sheety_password (str): The password for accessing the Sheety API.
                sheety_key (str): The API key for accessing the Sheety API.
                sheety_headers (dict): The headers required for making requests to the Sheety API.
                sheet_data (list): The flight data retrieved from the Sheety API.
            """
            self.sheety_password = sheety_password
            self.sheety_key = sheety_key
            self.sheety_headers = {
                "Authorization": sheety_password
            }
            self.sheet_data = self.get_flight_data()

    def get_flight_data(self):
            """
            Retrieves flight data from the Sheety API.

            Returns:
                list: A list of flight data.
            """
            with requests.get(f"{SHEETY_URL}/{self.sheety_key}/{SHEETY_PROJECT_NAME}/{PRICE_SHEET_NAME}", headers=self.sheety_headers) as response:
                response.raise_for_status()
                sheet_data = response.json()["prices"]
            return sheet_data

    def missing_iata_codes(self):
            """
            Returns a list of dictionaries containing the city and id of entries in the sheet_data
            where the iataCode is missing.

            Returns:
                list: A list of dictionaries with the city and id of entries with missing iataCode.
            """
            return [{"city": data["city"], "id": data["id"]} for data in self.sheet_data if len(data["iataCode"]) == 0]

    def update_iata_codes(self, code, id):
        """
        Updates the IATA code for a specific flight deal in the database.

        Args:
            code (str): The new IATA code to be updated.
            id (int): The ID of the flight deal to be updated.

        Raises:
            requests.HTTPError: If the HTTP request to update the data fails.

        Returns:
            None
        """
        update_data = {"price": {"iataCode": code}}
        response = requests.put(f"{SHEETY_URL}/{self.sheety_key}/{SHEETY_PROJECT_NAME}/{id}", headers=self.sheety_headers, json=update_data)
        response.raise_for_status()
    
    def get_user(self):
            """
            Retrieves the list of users from the Sheety API.

            Returns:
                list: A list of user objects.
            """
            with requests.get(f"{SHEETY_URL}/{self.sheety_key}/{SHEETY_PROJECT_NAME}/{USERS_SHEET_NAME}", headers=self.sheety_headers) as response:
                response.raise_for_status()
                return response.json()["users"]


    def add_user(self, first_name, last_name, email):
        """
        Adds a new user to the sheet.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email address of the user.

        Raises:
            requests.HTTPError: If there is an error in the HTTP request.

        Returns:
            None
        """
        params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        with requests.post(f"{SHEETY_URL}/{self.sheety_key}/{SHEETY_PROJECT_NAME}/{USERS_SHEET_NAME}", headers=self.sheety_headers, json=params) as response:
            response.raise_for_status()
            print(response.text)

    def create_user(self):
            """
            Creates a new user by collecting their first name, last name, and email.
            If the email is entered correctly twice, the user is added to the club.
            """
            print("Welcome to Manan's Flight Club.")
            print("We find the best flight deals and email you.")
            first_name = input("What is your first name?\n")
            last_name = input("What is your last name?\n")
            email = input("What is your email?\n")
            if email == input("Type your email again.\n"):
                print("You're in the club!")
                self.add_user(first_name, last_name, email)
            else:
                print("Email does not match. Please try again!")
