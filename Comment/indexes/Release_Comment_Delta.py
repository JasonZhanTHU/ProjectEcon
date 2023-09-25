import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import *

with open('../files/all_App_info.json', 'r') as f:
    data = json.load(f)

date_format = "%Y-%m-%d"
count = 0
odd = 0
array=[]
for key in data:
    if 'earliest_comment' in data[key] and data[key]['realInstalls'] > 1000000 and data[key]['released'] is not None:

        delta=datetime.strptime(data[key]['earliest_comment'], date_format)-datetime.strptime(data[key]['released'], date_format)
        array.append(delta.days)
        if abs(delta.days)>20 or delta.days<0:
            odd+=1

print(odd)
print(len(array))
print(odd/len(array))
plt.hist(array, bins='auto', alpha=0.7, rwidth=0.85)

# Add labels and title
plt.xlabel('Days')
plt.ylabel('App numbers')
plt.xlim(-50, 100)  # Adjust the x-axis limits
plt.ylim(0,100)  # Adjust the x-axis limits

plt.title('Number of days to get first comment')

# Show the plot
plt.show()

#datetime