import json

with open('../../files/ad_reviews.json', 'r') as f:
    data = json.load(f)

def is_substring(substring, main_string):
    return main_string.find(substring) != -1

new_dict={}

tot=0
for key in data:
    new_dict[key]={}
    for id in data[key]:
        if is_substring('change',data[key][id]['review'].lower()) or is_substring('turn',data[key][id]['review'].lower()) or is_substring('become',data[key][id]['review'].lower()) or is_substring('before',data[key][id]['review'].lower()) or is_substring('ago',data[key][id]['review'].lower()) or is_substring('used',data[key][id]['review'].lower()) or is_substring('different',data[key][id]['review'].lower()):
            new_dict[key][id]=data[key][id]
            tot+=1

with open('../../files/Specifics/Change_ads.json', 'w') as json_file:
    json.dump(new_dict, json_file, indent=4)

