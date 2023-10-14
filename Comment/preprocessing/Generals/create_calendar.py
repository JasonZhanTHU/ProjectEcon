import json
from datetime import date, timedelta

start_date = date(2009, 1, 1)
end_date = date(2025, 1, 1)
delta = timedelta(days=1)

date_list = []
current_date = start_date

while current_date <= end_date:
    date_list.append(current_date.strftime('%Y-%m-%d'))
    current_date += delta

# Save the list of date strings to a JSON file
with open("/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/calendar.json", 'w') as json_file:
    json.dump(date_list, json_file)

