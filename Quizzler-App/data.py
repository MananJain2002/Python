import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

with requests.get("https://opentdb.com/api.php", params=parameters) as response:
    response.raise_for_status()
    data = response.json()

question_data = data["results"]