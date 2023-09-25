import json
import os
import re
from datetime import *

with open('../../files/all_App_info.json', 'r') as f:
    data = json.load(f)

with open('../../files/Specifics/Estimate.json', 'r') as f:
    distribution = json.load(f)

with open('../../files/calendar.json', 'r') as f:
    calendar = json.load(f)

folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

Est_Download = {}
for key in calendar:
    Est_Download[key] = 0

date_format = "%Y-%m-%d"


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


def extract_date(str, installs):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(.*?)(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|$)'

    lines = re.findall(pattern, str, re.DOTALL)
    if len(lines) < 100:
        return
    release_datetime = datetime.strptime('9999-12-31', date_format)

    for line in lines:
        date = line[0].strip() if line[0] else line[3].strip()
        comment_datetime = datetime.strptime(date[:10], date_format)
        if release_datetime > comment_datetime:
            release_datetime = comment_datetime

    for i in range(0, 5000):
        str=(release_datetime + timedelta(days=i)).strftime("%Y-%m-%d")
        if str in Est_Download:
            Est_Download[str] += installs * distribution[i]
        else:
            return

count = 0
for key in file_names:
    count += 1
    print(count)
    if key not in data:
        continue
    file_path = os.path.join(folder_path, key)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    extract_date(content, data[key]['realInstalls'])

with open('../../files/Specifics/Estimate_Downloads.json', 'w') as json_file:
    json.dump(Est_Download, json_file, indent=4)
