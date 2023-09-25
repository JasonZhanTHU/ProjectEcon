import json
import os
import sys
sys.path.append('../../')
# from fields.phrase_location import *


def formalize_datetime(date_str):
    date_components = date_str.split()

    # Map the month abbreviation to its numerical representation
    month_dict = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }

    # Extract the year, month, and day
    year = date_components[2]
    month = month_dict[date_components[0]]
    day = date_components[1][:-1]  # Remove the comma
    day = day.zfill(2)

    # Create the formatted date string
    formatted_date_str = f"{year}-{month}-{day}"
    return formatted_date_str

with open('../../files/all_App_info.json', 'r') as f:
    data = json.load(f)



folder_path = os.path.expanduser("~/Downloads/all_reviews")
info_folder_path = os.path.expanduser("~/Downloads/all_infos")

file_names = os.listdir(info_folder_path)

count = 0

for file_name in file_names:
    temp = {}

    if file_name in data:
        temp=data[file_name]

    print(count)
    count += 1
    file_path = os.path.join(folder_path, file_name)
    info_file_path = os.path.join(info_folder_path, file_name)

    try:
        with open(info_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            content = json.loads(content)

            temp['developerAddress'] = content['developerAddress']
            # temp['country'] = phrase_address(content['developerAddress'])
            # temp['region'] = phrase_region(temp['country'])
            temp['adSupported'] = content['adSupported']
            temp['containsAds'] = content['containsAds']
            temp['price'] = content['price']
            temp['realInstalls'] = content['realInstalls']
            temp['developer'] = content['developer']
            temp['privacyPolicy'] = content['privacyPolicy']
            temp['genre'] = content['genre']
            if content['released'] is not None:
                temp['released'] = formalize_datetime(content['released'])

            data[file_name] = temp


    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading JSON from '{file_path}': {e}")

with open('../../files/all_App_info.json', 'w') as file:
    json.dump(data, file, indent=4)
