class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, price, dep_city_name, dep_airport_code, arrival_city_name,
                 arrival_airport_code, outbound_date, inbound_date, stop_overs=0, via_city=""):
        self.price = price
        self.dep_city_name = dep_city_name
        self.dep_airport_code = dep_airport_code
        self.arrival_city_name = arrival_city_name
        self.arrival_airport_code = arrival_airport_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.stop_overs = stop_overs
        self.stop_over_city = via_city
