import pandas
import json
from fields.phrase_name import identify_through_name, identify_through_ner
from fields.phrase_location import phrase_address
import ast

df = pandas.read_excel('Location/main4.py/random_sample.xlsx')

df['individual'] = None
df['country'] = None

with open('files/all_permissions.json') as f:
    all_permissions = json.load(f)

for item in all_permissions:
    df[item] = 0

for i in range(0, 500):

    print('processing.py item', i)

    policy_url = df.loc[i, 'policy_url']
    developer = df.loc[i, 'developer']

    flag = 0
    flag |= identify_through_name(developer)
    flag |= identify_through_ner(developer)

    if flag == 0:
        df.loc[i, 'individual'] = 1
    else:
        df.loc[i, 'individual'] = 0

    developer_address = df.loc[i, 'developer_address']

    try:
        country = phrase_address(developer_address)
        df.loc[i, 'country'] = country
    except Exception as e:
        df.loc[i, 'country'] = e

    permissions = df.loc[i, 'permissions']

    if type(permissions) != type('str'):
        continue

    array_data = ast.literal_eval(permissions)
    for permission in array_data:
        df.loc[i, permission] = 1

df.to_excel('processed_sample.xlsx')

# sudo venv/bin/python3.10 main4.py
