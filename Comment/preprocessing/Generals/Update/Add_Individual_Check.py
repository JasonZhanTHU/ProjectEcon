import json
import os
import numpy

import sys

sys.path.append('../../')
from fields.phrase_name import *

current_directory = os.getcwd()
print(current_directory)

with open('../../files/all_App_info.json', 'r') as f:
    data = json.load(f)

count = 0
for key in data:

    print(count)
    count += 1

    if 'individual' in data[key]:
        continue

    flag = 0
    flag |= identify_through_name(data[key]['developer'])
    flag |= identify_through_ner(data[key]['developer'])

    if flag == 0:
        data[key]['individual'] = 1
    else:
        data[key]['individual'] = 0

with open('../../files/all_App_info.json', 'w') as f:
    json.dump(data, f, indent=4)


#   sudo ../../../venv/bin/python3.10 add_individual_check.py
