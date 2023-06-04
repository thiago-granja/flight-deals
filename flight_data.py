import json
from pprint import pprint

class FlightData:
    #This class is responsible for structuring the flight data.

    with open("sheet_data.json") as sheet_file:
        sheet_data = json.load(sheet_file)

        with open('flights_found.json') as json_file:
            data = json.load(json_file)

            for flight in data['data']:
                arrival_city = flight['cityTo']
                price = flight['price']
                for row in sheet_data['prices']:
                    if arrival_city == row['city'] and price <= row['lowestPrice']:
                        departure_city = flight['cityFrom']
                        departure_airport = flight['flyFrom']
                        arrival_airport = flight['flyTo']
                        nights_in_destination = flight['nightsInDest']
                        outbound_date = flight['local_departure'].split("T")[0]
                        inbound_date = flight['route'][1]['local_departure'].split("T")[0]
                        print(f"Low price alert! Only R${price} to fly from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, on {outbound_date} to {inbound_date}.")
