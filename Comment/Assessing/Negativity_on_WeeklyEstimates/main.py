from Gather_Comments import gather_comments
import pandas as pd
from datetime import *
import json
import matplotlib.pyplot as plt

date_format = "%Y-%m-%d"

with open('setup.json', 'r') as f:
    specs = json.load(f)
with open('period.json', 'r') as f:
    period = json.load(f)


plt.figure(figsize=(25, 15))


for key in specs:
    spec = specs[key]
    comments, info = gather_comments(spec)

    sorted_dict = dict(sorted(comments.items(), key=lambda x: x[0]))

    x_axis = []
    result = []

    cur={}
    cur['interval_start'] = period['interval_start']
    cur['interval_end'] = period['interval_end']
    for i in range(0, 100):
        tot = 0
        cnt = 0
        for i in sorted_dict.keys():
            if i >= cur['interval_start'] and i <= cur['interval_end']:
                tot += sorted_dict[i]
                cnt += 1

        if cnt != 0:
            tot /= cnt

        result.append(tot)

        cur['interval_start'] = pd.to_datetime(cur['interval_start']) + pd.DateOffset(days=7)
        cur['interval_start'] = str(cur['interval_start'])[:10]

        cur['interval_end'] = pd.to_datetime(cur['interval_end']) + pd.DateOffset(days=7)
        cur['interval_end'] = str(cur['interval_end'])[:10]

        x_axis.append(cur['interval_start'])
    plt.plot(x_axis, result, label=key, marker='o', linestyle='-')
    print(x_axis)



def add_verticle(str, label):
    for x in x_axis:
        if str < x:
            plt.axvline(x=x, color='red', linestyle='--', label=label)
            return


#add_verticle('2016-04-14', 'GDPR Announced')
add_verticle('2018-05-25', 'GDPR Implemented')

showed = []
for i in range(0, len(x_axis), 25):
    showed.append(x_axis[i])

plt.xticks(showed)
plt.xlabel('Week')
plt.ylabel('Negative Comment Percentage')
plt.legend()
plt.grid(True)
plt.show(block=True)
