import json
import matplotlib.pyplot as plt

with open('../../files/Specifics/Estimate_Downloads.json', 'r') as f:
    data = json.load(f)


mx=-99999
at=''
for day in data:
    if data[day]>mx:
        mx=data[day]
        at=day

print(at)

data = {key:value for key, value in data.items() if value > 30000000}


categories = list(data.keys())
counts = list(data.values())

# Create a bar chart
plt.bar(categories, counts)

# Add labels and a title
plt.xlabel("Categories")
plt.ylabel("Counts")
plt.title("Bar Chart of Categories")

# Display the chart
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()