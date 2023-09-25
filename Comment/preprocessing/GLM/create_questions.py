import json
import os
import re


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


def process(str):
    result = re.split(r'[,.!?]|but|except', str)
    res = ""
    for s in result:
        if (is_substring('ads', s) or is_substring('Ads', s)):
            res += s + '.'
    return res


current_directory = os.getcwd()
print(current_directory)

with open('../../files/ad_reviews.json', 'r') as input_file:
    content = json.load(input_file)

questions = {}
all = 0
for key in content:

    print(key)

    cur_dict = {}
    count = 0

    for i in content[key]:
        cur_dict[count] = process(content[key][i]['review'])
        count += 1

        cur_dict[count] = 'clear'
        count += 1
    questions[key] = cur_dict
    all += len(content[key]) * 2

print(all)

json_filename = '../../files/GLM/questions_reviews.json'
with open(json_filename, 'w') as json_file:
    json.dump(questions, json_file, indent=4)
