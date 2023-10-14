import json
import os
import numpy
import sys


def count_negative(ads):
    cur = 0
    for id in ads:
        if ads[id]['sentiment'] == 'POSITIVE':
            continue
        cur += 1
    return cur


with open('../../files/all_App_info.json', 'r') as f:
    data = json.load(f)

with open('../../files/ad_reviews.json', 'r') as f:
    reviews_ad = json.load(f)

with open('../../files/corp_reviews.json', 'r') as f:
    reviews_tot = json.load(f)

count = 0
for key in data:
    if key in reviews_tot and reviews_tot[key]:
        data[key]['review_sum'] = reviews_tot[key]
    else:
        data[key]['review_sum'] = 1
    if key in reviews_ad:
        data[key]['ad_complaints'] = count_negative(reviews_ad[key])
        data[key]['ad_positive'] = len(reviews_ad[key]) - data[key]['ad_complaints']
    else:
        data[key]['ad_complaints'] = 0
        data[key]['ad_positive'] = 0

with open('../../files/all_App_info.json', 'w') as f:
    json.dump(data, f, indent=4)


