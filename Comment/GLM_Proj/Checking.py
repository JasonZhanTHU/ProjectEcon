
import json
import os

folder_path = os.path.expanduser("~/Downloads/all_reviews")

file_names = os.listdir(folder_path)

count=0

count2=0
for file in file_names:

    print(count2)
    count2+=1
    file_path = os.path.join(folder_path, file)

    with open(file_path, 'r') as f:
        data = json.load(f)
    for item in data:
        if 'sentiment' in item:
            count+=1
            break
        else:
            break

print(count)