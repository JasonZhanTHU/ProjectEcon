import json
import os

date_format = "%Y-%m-%d"

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'r') as f:
    data = json.load(f)
with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/ad_reviews.json', 'r') as f:
    ad_reviews = json.load(f)

folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

count = 0

rem = []
# 打印所有文件名
for key in file_names:
    if key not in data:
        continue
    if data[key]['genre'] not in rem:
        rem.append(data[key]['genre'])

print(rem)


