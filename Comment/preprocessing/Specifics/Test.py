import json
import os
import re

folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

data_lists = []

count = 0
# 打印所有文件名

with open('../../files/all_App_info.json', 'r') as f:
    app_data = json.load(f)

print("hehe it is here")
count1=0
count2=0
for file in file_names:

    if not file in app_data.keys():
        count1+=1
    else:
        count2+=1

print(count1)
print(count2)
print(count1+count2)


#92539
#19332
