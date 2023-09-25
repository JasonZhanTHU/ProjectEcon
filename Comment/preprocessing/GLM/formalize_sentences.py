import json
import os
import re


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


def process(str):
    result = re.split(r'[,.!?]|but|except', str)
    res = ""
    for s in result:
        if is_substring('ads', s) or is_substring('Ads', s) or is_substring('privacy', s) or is_substring('advertise',
                                                                                                          s):
            res += s + '.'
    res = res.replace('ads ', 'advertisements')
    return res


current_directory = os.getcwd()
print(current_directory)

with open('../../files/ad_reviews.json', 'r') as input_file:
    content = json.load(input_file)

questions = {}
all = 0
for key in content:
    for i in content[key]:
        content[key][i]['review'] = process(content[key][i]['review'])

json_filename = '../../files/GLM/formalized_ad_reviews.json'
with open(json_filename, 'w') as json_file:
    json.dump(content, json_file, indent=4)
