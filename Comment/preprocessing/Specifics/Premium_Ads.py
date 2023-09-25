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
        if is_substring('premium',data[key][id]['review'].lower()) or is_substring('pay',data[key][id]['review'].lower()):
            new_dict[key][id]=data[key][id]
            tot+=1

with open('../../files/Specifics/Premium_Ads.json', 'w') as json_file:
    json.dump(new_dict, json_file, indent=4)

