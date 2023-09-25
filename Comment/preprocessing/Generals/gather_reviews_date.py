import json
import os
import re

data = {}


def extract_date(str, filename):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(.*?)(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|$)'

    lines = re.findall(pattern, str, re.DOTALL)

    for line in lines:
        date = line[0].strip() if line[0] else line[3].strip()
        if not date[:10] in data:
            data[date[:10]] = 0
        data[date[:10]] += 1


folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

data_lists = []

count = 0
# 打印所有文件名
for file_name in file_names:
    print(count)
    count += 1
    file_path = os.path.join(folder_path, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            extract_date(content, file_name)

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading JSON from '{file_path}': {e}")

data = sorted(data.items())
data = dict(data)

with open('../../files/all_reviews_date.json', 'w') as f:
    json.dump(data, f, indent=4)
