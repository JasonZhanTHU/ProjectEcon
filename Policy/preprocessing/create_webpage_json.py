import pandas
import json
import ast
import os
import sys
import random

sys.path.append('../')
from webpage.webpage import get_privacy_text

df = pandas.read_excel('../files/random_sample.xlsx')


with open('../files/webpages.json', 'r') as input_file:
    data = json.load(input_file)

array = list(range(df.shape[0]))
random.shuffle(array)

for i in array:
    if str(i) in data:
        continue

    print(df.loc[i, 'policy_url'])
    try:
        text = get_privacy_text(df.loc[i, 'policy_url'])
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        text = text.replace('  ', ' ')
        print(text)

        data[i] = text
    except Exception as e:
        print(e)

    if i % 10 == 0:
        json_filename = '../files/webpages.json'
        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

print(data)

json_filename = '../files/webpages.json'
with open(json_filename, 'w') as json_file:
    json.dump(data, json_file, indent=4)
