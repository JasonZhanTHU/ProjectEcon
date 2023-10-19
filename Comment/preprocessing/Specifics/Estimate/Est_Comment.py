import json
import os
from datetime import *
import pandas as pd


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


count = 0
result = [0] * 900

date_format = "%Y-%m-%d"

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'r') as f:
    data = json.load(f)
with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/ad_reviews.json', 'r') as f:
    ad_reviews = json.load(f)


def extract_date(reviews, released):
    if len(reviews) < 100:
        return

    global count
    count += 1
    print(count)

    # release_datetime = datetime.strptime('9999-12-31', date_format)
    #
    # for review in reviews:
    #     date = review['date']
    #     comment_datetime = datetime.strptime(date[:10], date_format)
    #     if release_datetime > comment_datetime:
    #         release_datetime = comment_datetime

    for review in reviews:
        comment_datetime = datetime.strptime(review['date'][:10], date_format)
        delta = comment_datetime - released
        if delta.days >= 900 or delta.days<0:
            continue
        result[delta.days] += 1 / len(reviews)

    return released


def operate(sectors):
    folder_path = os.path.expanduser("~/Downloads/all_reviews")

    file_names = os.listdir(folder_path)

    count = 0

    # 打印所有文件名
    for key in file_names:
        if key not in data:
            continue
        if data[key]['released'] is None:
            continue
        if key not in ad_reviews:
            continue
        # if 'earliest_comment' not in data[key]:
        #     continue
        # if data[key]['earliest_comment'] > '2016':
        #     continue
        if sectors != [] and data[key]['genre'] not in sectors:
            continue

        file_path = os.path.join(folder_path, key)

        release_datetime = datetime.strptime(data[key]['released'], date_format)

        with open(file_path, 'r', encoding='utf-8') as f:
            reviews = json.load(f)
            res = extract_date(reviews, release_datetime)

    with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/Specifics/Estimate_Count.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
