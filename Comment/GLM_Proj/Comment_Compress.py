import json
import os

folder_path = os.path.expanduser("~/autodl-tmp/all_reviews")

file_names = os.listdir(folder_path)

content = {}


count=0

for file in file_names:

    count+=1
    print(count)


    content[file] = {}
    content[file]['Positive'] = {}
    content[file]['Negative'] = {}

    file_path = os.path.join(folder_path, file)
    with open(file_path, 'r') as f:
        data = json.load(f)
    for item in data:

        date=item['date'][:10]

        if 'lable' in item['sentiment'] and item['sentiment'][0]['label'] == 'NEGATIVE' and item['sentiment'][0]['lable'] > 0.9:

            if item['date'] not in content[file]['Negative']:
                content[file]['Negative'][date] = 0

            content[file]['Negative'][date] += 1

        else:
            if item['date'] not in content[file]['Positive']:
                content[file]['Positive'][date] = 0

            content[file]['Positive'][date] += 1

save_path = os.path.expanduser("~/autodl-tmp/compressed.json")
with open(save_path, 'r') as f:
    json.dump(content, f, indent=4)
