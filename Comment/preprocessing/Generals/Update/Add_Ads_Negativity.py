import json

with open('../../../files/ad_reviews.json', 'r') as f:
    data = json.load(f)

with open('../../../files/GLM/formalized_ad_reviews.json', 'r') as f:
    res = json.load(f)

for key in data:
    for id in data[key]:
        data[key][id]['sentiment'] = res[key][id]['sentiment'][0]['label']

with open('../../../files/ad_reviews.json', 'w') as f:
    json.dump(data, f, indent=4)
