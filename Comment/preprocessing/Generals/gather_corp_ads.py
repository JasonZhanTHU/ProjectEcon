import json
import os
import re


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


def extract_date(str, filename):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(.*?)(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|$)'

    lines = re.findall(pattern, str, re.DOTALL)

    return len(lines)


folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

data={}
count = 0
# 打印所有文件名
for file_name in file_names:
    print(count)
    count += 1
    file_path = os.path.join(folder_path, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            data[file_name] = extract_date(content, file_name)

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading JSON from '{file_path}': {e}")

with open('../../files/corp_reviews.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
