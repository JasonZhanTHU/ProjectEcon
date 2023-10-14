import json
import os
from datetime import *
import pandas as pd


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


result = [0] * 1800

date_format = "%Y-%m-%d"

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'r') as f:
    data = json.load(f)
with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/ad_reviews.json', 'r') as f:
    ad_reviews = json.load(f)


def extract_date(reviews, ad_reviews, upper_limit):
    if len(reviews) < 100:
        return
    release_datetime = datetime.strptime('9999-12-31', date_format)

    for review in reviews:
        date = review['date']
        comment_datetime = datetime.strptime(date[:10], date_format)
        if release_datetime > comment_datetime:
            release_datetime = comment_datetime

    tot = 0

    for key in ad_reviews:
        ad = ad_reviews[key]

        if ad['sentiment'] != 'NEGATIVE':
            continue
        if ad['date'] >= upper_limit:
            continue
        tot += 1

    for ad in ad_reviews.values():
        if ad['sentiment'] != 'NEGATIVE':
            continue
        if ad['date'] >= upper_limit:
            continue
        comment_datetime = datetime.strptime(ad['date'][:10], date_format)
        delta = comment_datetime - release_datetime
        result[delta.days] += 1 / tot

    return release_datetime


folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

count = 0
tot = 0

# 打印所有文件名
for key in file_names:
    count += 1
    print(count)
    if key not in data:
        continue
    if data[key]['released'] is None:
        continue
    if key not in ad_reviews:
        continue
    if 'earliest_comment' not in data[key]:
        continue
    if data[key]['earliest_comment'] > '2016':
        continue
    if key < "com.panotogomo.nuclear":
        continue
    file_path = os.path.join(folder_path, key)
    upper_limit = str(pd.to_datetime(data[key]['earliest_comment']) + pd.DateOffset(days=1800))

    with open(file_path, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
        res = extract_date(reviews, ad_reviews[key], upper_limit)

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/Specifics/Estimate_Ads.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)
# with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)