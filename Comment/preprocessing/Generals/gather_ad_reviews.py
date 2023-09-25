import json
import os
import re


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


dict = {}


def extract_date(str, filename):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(.*?)(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|$)'

    lines = re.findall(pattern, str, re.DOTALL)

    count2 = 0

    cur_dict = {}
    for line in lines:
        temp = {}
        date = line[0].strip() if line[0] else line[3].strip()
        review = line[1].strip() if line[1] else " "

        if not is_substring(' ads', review) and not is_substring('Ads', review) and not is_substring('advertise',
                                                                                                     review) and not is_substring(
                'privacy', review):
            continue

        temp['date'] = date
        temp['review'] = review

        cur_dict[count2] = temp

        dict[filename] = cur_dict
        count2 += 1

    return dict


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
            dict = extract_date(content, file_name)

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading JSON from '{file_path}': {e}")

with open('../../files/ad_reviews.json', 'w') as json_file:
    json.dump(dict, json_file, indent=4)
