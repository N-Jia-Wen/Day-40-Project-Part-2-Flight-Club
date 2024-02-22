from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager_obj = DataManager()
flight_search_obj = FlightSearch()
notification_manager = NotificationManager()

# To add IATA codes of the cities in the Google sheet, if needed:
for vacation_destination in data_manager_obj.flight_deal_data:

    # Fills in IATA city codes if Google sheet is blank:
    if vacation_destination["iataCode"] == "":
        flight_search_obj.find_iata_code(vacation_destination["city"])
        vacation_destination["iataCode"] = flight_search_obj.iata_code
        data_manager_obj.update_sheet(vacation_destination)

    # This method returns a FlightData object with all the necessary info saved as attributes:
    flight_data = flight_search_obj.find_flight_deals(vacation_destination["iataCode"])

    # flight_data is set to None of there are no flights found within the specified parameters in flight_search
    if flight_data is not None:

        # Checks if cheapest flight found is less expensive than maximum flight price specified in Google sheet:
        if flight_data.price < vacation_destination["lowestPrice"]:
            notification_manager.send_email(price=flight_data.price,
                                            dep_city=flight_data.dep_city_name,
                                            dep_airport=flight_data.dep_airport_code,
                                            arrival_city=flight_data.arrival_city_name,
                                            arrival_airport=flight_data.arrival_airport_code,
                                            outbound_date=flight_data.outbound_date,
                                            inbound_date=flight_data.inbound_date,
                                            no_of_stopovers=flight_data.stop_overs,
                                            stopover_city=flight_data.stop_over_city,
                                            users_data=data_manager_obj.users_data)

            print(f"Email with info for cheap flight to {flight_data.arrival_airport_code} sent!")
        else:
            print(f"Flight to {flight_data.arrival_airport_code} is too expensive. Nothing was sent.")
