import os
import requests
from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheet_data = self.get_sheet_data()
        self.flight_search = FlightSearch(sheet_data_input=self.sheet_data)
        self.flight_search.update_destinations()
        self.flight_data = self.flight_search.search_flights()

    api_user = os.environ['SHEETY_USER']
    api_token = os.environ['SHEETY_TOKEN']
    api_project = 'flightDeals'
    api_sheet = 'prices'
    api_endpoint = f"https://api.sheety.co/{api_user}/{api_project}/{api_sheet}"
    headers = {
        'Authorization': f'Basic {api_token}'
    }

    def get_sheet_data(self):
        response = requests.get(url=self.api_endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_iata_codes(self):
        for row in self.sheet_data['prices']:
            if row['iataCode'] == '':
                column_id = row['id']
                iata_code = self.flight_search.search_iata_code(city_name=row['city'])
                dataToSend = {'price': {'iataCode': iata_code}}
                response = requests.put(url=f"{self.api_endpoint}/{column_id}", json=dataToSend,
                                        headers=self.headers)
                response.raise_for_status()
