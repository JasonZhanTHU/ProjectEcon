import json
import os
import re
from datetime import *


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


date_format = "%Y-%m-%d"


def extract_date(reviews):

    if len(reviews) < 100:
        return
    release_datetime = datetime.strptime('9999-12-31', date_format)

    for review in reviews:
        date = review['date']
        comment_datetime = datetime.strptime(date[:10], date_format)
        if release_datetime > comment_datetime:
            release_datetime = comment_datetime
    return release_datetime


with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'r') as f:
    data = json.load(f)

folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

count = 0
tot = 0
# 打印所有文件名
for key in file_names:
    count += 1
    print(count)
    if key not in data:
        continue
    if data[key]['released'] is None:
        continue
    file_path = os.path.join(folder_path, key)

    with open(file_path, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
        res = extract_date(reviews)

        if res is not None:
            data[key]['earliest_comment'] = res.strftime("%Y-%m-%d")

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
