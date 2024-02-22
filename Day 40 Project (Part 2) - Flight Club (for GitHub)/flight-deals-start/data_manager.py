import requests

SHEETY_ENDPOINT = "Enter the Sheety API endpoint for the entire Google sheet you are using here."


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        deal_get_response = requests.get(url=f"{SHEETY_ENDPOINT}/flightDeals")
        users_get_response = requests.get(url=f"{SHEETY_ENDPOINT}/users")
        self.flight_deal_data = deal_get_response.json()["flightDeals"]
        self.users_data = users_get_response.json()["users"]


    def update_sheet(self, updated_vacation_destination):
        # After self.sheet_data dictionary is updated in main.py, execute this:

        id_num = updated_vacation_destination["id"]
        specific_sheety_endpoint = f"{SHEETY_ENDPOINT}/{id_num}"
        changed_data = {
            "flightDeal": {
                "iataCode": updated_vacation_destination["iataCode"]
            }
        }
        put_response = requests.put(url=specific_sheety_endpoint, json=changed_data)
        put_response.raise_for_status()
