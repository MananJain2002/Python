from dotenv import load_dotenv
from datetime import datetime
import requests, os

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("USER")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

headers = {
        "X-USER-TOKEN": TOKEN
}

def create_user():
    """
    Creates a user by sending a POST request to the PIXELA_ENDPOINT with the user parameters.

    Returns:
        None
    """
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    with requests.post(url=PIXELA_ENDPOINT, json=user_params) as response:
        print(response.text)

def create_graph():
    """
    Creates a graph on the Pixela API.

    This function prompts the user to enter the necessary information for creating a graph,
    such as the graph ID, name, unit, type, and color. It then sends a POST request to the
    Pixela API with the provided information to create the graph.

    Returns:
        None
    """
    global GRAPH_ID
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

    while True:
        GRAPH_ID = input("Please enter a graph ID: ")
        name = input("Please enter a name for the graph: ")
        unit = input("Please enter a unit for the graph: ")
        type_ = input("Please enter a type for the graph (int or float): ")

        while True:
            color = input("Please enter a color for the graph (shibafu, momiji, sora, ichou, ajisai, kuro): ")
            if color in ['shibafu', 'momiji', 'sora', 'ichou', 'ajisai', 'kuro']:
                break
            else:
                print("Invalid color. Please enter one of the following: shibafu, momiji, sora, ichou, ajisai, kuro.")

        if type_ not in ['int', 'float']:
            print("Invalid type. Please enter 'int' or 'float'.")
            continue

        graph_config = {
            "id": GRAPH_ID,
            "name": name,
            "unit": unit,
            "type": type_,
            "color": color
        }

        headers = {
            "X-USER-TOKEN": TOKEN
        }

        with requests.post(url=graph_endpoint, json=graph_config, headers=headers) as response:
            if response.status_code == 200:
                print(response.text)
                break
            else:
                print("Error creating graph. Please try again.")

def get_quantity():
    """
    Prompts the user to enter the number of hours they have cycled and returns it as a string.

    Returns:
        str: The number of hours cycled, rounded to 2 decimal places.
    """
    while True:
        try:
            quantity = float(input("How many hours have you cycled? "))
            return str(round(quantity, 2))
        except ValueError:
            print("Please enter valid time")

def get_date():
    """
    Prompts the user to enter a date in the format yyyymmdd and validates the input.

    Returns:
        str: The validated date in the format yyyymmdd.
    """
    while True:
        date = input("Please enter date in format yyyymmdd: ")
        if len(date) != 8 or not date.isdigit():
            print("Invalid date format. Please try again.")
        else:
            return date

def add_entry():
    """
    Adds an entry to the habit tracker graph.

    This function sends a POST request to the pixel creation endpoint of the Pixela API
    to add a new entry to the specified graph. The date of the entry is set to the current
    date and the quantity is obtained from the `get_quantity` function.

    Parameters:
        None

    Returns:
        None
    """
    today = datetime.now()
    pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_creation_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": get_quantity()
    }
    with requests.post(url=pixel_creation_endpoint, json=pixel_creation_params, headers=headers) as response:
        print(response.text)


def update_entry():
    """
    Updates the entry for a specific date in the habit tracker graph.

    This function sends a PUT request to the pixela API to update the quantity of a specific date's entry in the graph.

    Parameters:
    None

    Returns:
    None
    """
    pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{get_date()}"
    pixel_update_params = {
        "quantity": get_quantity()
    }
    with requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers) as response:
        print(response.text)

def delete_entry():
    """
    Deletes an entry from the habit tracker graph.

    This function sends a DELETE request to the Pixela API to delete an entry from the specified graph.
    The entry to be deleted is determined by the current date.

    Returns:
        None
    """
    pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{get_date()}"
    with requests.delete(url=pixel_delete_endpoint, headers=headers) as response:
        print(response.text)

def cycle_tracking():
    """
    Function to track cycles and perform actions based on user input.

    The function prompts the user to choose an action: add, update, delete, or create a new graph.
    It then calls the corresponding function based on the user's choice.
    The function continues to prompt the user until they choose to exit.

    Parameters:
    None

    Returns:
    None
    """
    actions = {
        'add': add_entry,
        'update': update_entry,
        'delete': delete_entry,
        'create': create_graph
    }
    while True:
        action = input("Do you want to add for today, update, delete any date, or create a new graph? Please type 'add', 'update', 'delete', 'create', or type 'exit' to exit: ").lower()
        if action in actions:
            actions[action]()
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

cycle_tracking()