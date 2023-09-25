import json
import os
import re
from datetime import *


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


tot = 0

result = [0] * 10000

date_format = "%Y-%m-%d"


def extract_date(str, file):
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

    for line in lines:
        date = line[0].strip() if line[0] else line[3].strip()
        comment_datetime = datetime.strptime(date[:10], date_format)
        delta = comment_datetime - release_datetime
        result[delta.days] += 1 / len(lines)
    global tot
    tot += 1
    return release_datetime


with open('../../files/all_App_info.json', 'r') as f:
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
        content = f.read()

    res = extract_date(content, key)
    if res is not None:
        data[key]['earliest_comment'] = res.strftime("%Y-%m-%d")

for i in range(0, len(result)):
    result[i] /= tot

with open('../../files/Specifics/Estimate.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)
with open('../../files/all_App_info.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
