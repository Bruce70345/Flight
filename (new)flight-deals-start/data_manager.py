import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/256983a09bc8c1bb40914b84395134d0/flightDealsNew/prices"
HEADERS = {
        "Authorization": f"Bearer 123",
        "Content-Type": "application/json",
    }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
        # if "prices" in data:
        #     self.destination_data = data["prices"]
        #     return self.destination_data
        # else:
        #     print("Error: 'prices' key not found in the data.")
        #     return None
        self.destination_data = data["prices"]
        # print(data)
        # pprint(self.destination_data)
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
            )
            # print(response.text)
