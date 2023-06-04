from data_manager import DataManager
from notification_manager import NotificationManager
import json

data_manager = DataManager()

# creates flights_found.json (stores found flights information)
with open('flights_found.json', mode='w') as json_file:
    data = json.dumps(data_manager.flight_data, indent=4)
    json_file.write(data)

# creates sheet_data.json (stores gsheet information)
with open('sheet_data.json', mode='w') as sheet_file:
    data = json.dumps(data_manager.sheet_data, indent=4)
    sheet_file.write(data)
