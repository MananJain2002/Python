class FlightData:

    class FlightData:
        def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, stop_overs=0, via_city=""):
            """
            Initialize a FlightData object with the given parameters.

            Args:
                price (float): The price of the flight.
                origin_city (str): The city of departure.
                origin_airport (str): The airport of departure.
                destination_city (str): The city of arrival.
                destination_airport (str): The airport of arrival.
                out_date (str): The date of departure.
                return_date (str): The date of return.
                stop_overs (int, optional): The number of stopovers. Defaults to 0.
                via_city (str, optional): The city of the stopover. Defaults to "".
            """
            self.price = price
            self.origin_city = origin_city
            self.origin_airport = origin_airport
            self.destination_city = destination_city
            self.destination_airport = destination_airport
            self.out_date = out_date
            self.return_date = return_date
            self.stop_overs = stop_overs
            self.via_city = via_city
