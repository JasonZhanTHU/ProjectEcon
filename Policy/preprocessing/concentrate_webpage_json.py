import pandas
import json
import re
import os
import sys
import random


def is_substring(substring, main_string):
    return main_string.lower().find(substring) != -1


with open('../files/words.json', 'r') as f:
    key_words = json.load(f)


def select_words(str):
    for key in key_words:
        if is_substring(' ' + key + ' ', ' ' + str.lower()) or is_substring(' ' + key + '.', ' ' + str.lower()):
            return True
    return False


def process(str):
    str = str.replace('\t', ' ')
    str = str.replace('\r', ' ')
    result = re.split(r'[.!?]|but|except|    ', str)
    res = ""
    for s in result:
        if select_words(s):
            res += s + '.'
    return res


with open('../files/webpages.json', 'r') as input_file:
    data = json.load(input_file)

for id in data:
    data[id] = process(data[id])

with open('../files/processed_webpages.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
