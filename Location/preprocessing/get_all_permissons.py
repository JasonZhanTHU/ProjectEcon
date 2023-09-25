import pandas
import ast
import json

df = pandas.read_excel('../main4.py/random_sample.xlsx')

element_map = {}


def create_element_frequency_map(array):
    for element in array:
        if element in element_map:
            element_map[element] += 1
        else:
            element_map[element] = 1
    return element_map


def save_map_to_json(file_path, data_map):
    with open(file_path, 'w') as json_file:
        json.dump(data_map, json_file)


for i in range(0, 500):

    permissions = df.loc[i, 'permissions']
    if type(permissions) != type('str'):
        continue
    array_data = ast.literal_eval(permissions)
    create_element_frequency_map(array_data)

save_map_to_json('../files/all_permissions.json', element_map)
