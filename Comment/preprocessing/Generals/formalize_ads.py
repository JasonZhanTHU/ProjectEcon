import json
import os
import re


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


def extract_date(str):

    array = []

    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(.*?)(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|$)'

    lines = re.findall(pattern, str, re.DOTALL)

    count2 = 0

    for line in lines:
        temp = {}
        date = line[0].strip() if line[0] else line[3].strip()
        review = line[1].strip() if line[1] else " "

        temp['date'] = date
        temp['review'] = review

        array.append(temp)

    return array


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
        dict = extract_date(content)
        with open(file_path, 'w') as f:
            json.dump(dict, f, indent=4)

    except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading JSON from '{file_path}': {e}")

