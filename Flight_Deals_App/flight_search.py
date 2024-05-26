from flight_data import FlightData
import requests, os

TEQUILA_URL = "https://api.tequila.kiwi.com"

class FlightSearch:

    class FlightSearch:
        def __init__(self, tequila_api):
            """
            Initializes a new instance of the FlightSearch class.

            Args:
                tequila_api (str): The API key for the Tequila API.

            Returns:
                None
            """
            self.tequila_headers = {"apikey": tequila_api}

    def get_iata_codes(self, city):
        """
        Retrieves the IATA code for a given city using the Tequila API.

        Args:
            city (str): The name of the city for which to retrieve the IATA code.

        Returns:
            str: The IATA code for the specified city.

        Raises:
            requests.HTTPError: If there is an error in the HTTP request.

        """
        tequila_params = {"term": city, "location_types": "city"}
        response = requests.get(f"{TEQUILA_URL}/locations/query", headers=self.tequila_headers, params=tequila_params)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]
    
    def get_best_price(self, fly_from, fly_to, date_from, date_to):
        """
        Retrieves the best price for a flight based on the given parameters.

        Args:
            fly_from (str): The code of the departure airport.
            fly_to (str): The code of the destination airport.
            date_from (str): The start date for the flight search (in the format "YYYY-MM-DD").
            date_to (str): The end date for the flight search (in the format "YYYY-MM-DD").

        Returns:
            FlightData or None: An instance of the FlightData class representing the best flight option,
            or None if no flights are found.

        Raises:
            HTTPError: If there is an error in the HTTP request.

        """
        tequila_params = query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        with requests.get(f"{TEQUILA_URL}/v2/search", headers=self.tequila_headers, params=tequila_params) as response:
            response.raise_for_status()

            try:
                data = response.json()["data"][0]
            except IndexError:
                query["max_stopovers"] = 1
                response = requests.get(
                    url=f"{TEQUILA_URL}/v2/search",
                    headers=self.tequila_headers,
                    params=query,
                )
                if len(response.json()) == 0:
                    return None
                data = response.json()["data"][0]
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0]
                )
                return flight_data