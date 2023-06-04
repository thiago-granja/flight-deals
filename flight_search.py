import datetime
import requests

today = datetime.datetime.today()
start_date_formatted = (today + datetime.timedelta(days=21)).strftime("%d/%m/%Y")
end_date_formatted = (today + datetime.timedelta(days=120)).strftime("%d/%m/%Y")


class FlightSearch:
    #  This class is responsible for talking to the Flight Search API.

    def __init__(self, sheet_data_input):
        self.sheet_data = sheet_data_input
        self.api_key = 'dqWay9X3TCM-I3fR05y_PySg0QAZkw68'
        self.locations_endpoint = 'http://api.tequila.kiwi.com/locations/query'
        self.api_endpoint = 'http://api.tequila.kiwi.com/v2/search'
        self.headers = {'apikey': self.api_key}
        self.parameters = {
            'fly_from': 'SAO,JTC',
            'fly_to': 'PAR,BER,TYO,SYD,IST,KUL,NYC,SFO,CPT,LON,MIL,MOW,ROM',
            'curr': 'BRL',
            'date_from': start_date_formatted,
            'date_to': end_date_formatted,
            # 'locale': 'pt',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'max_stopovers': 0,
            'price_to': 15000,
            'only_working_days': True,
            'limit': 1000,
            'one_for_city': 1,


        }

    def update_destinations(self):
        fly_to_string = ''
        for row in self.sheet_data['prices']:
            fly_to_string += (f'{row["iataCode"]},')
        self.parameters['fly_to'] = fly_to_string[:-1]

    def search_flights(self):
        response = requests.get(url= self.api_endpoint, params=self.parameters, headers=self.headers)
        return response.json()

    def search_iata_code(self, city_name):
        response = requests.get(url=self.locations_endpoint, headers=self.headers, params={'term': city_name})
        return response.json()['locations'][0]['code']
