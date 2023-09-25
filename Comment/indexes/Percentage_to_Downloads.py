import json
import numpy
import matplotlib.pyplot as plt

with open('../files/all_App_info.json', 'r') as f:
    info = json.load(f)


percentage=[]
downloads=[]
for key in info:
    cur=info[key]['ad_complaints']/info[key]['review_sum']
    percentage.append(cur)
    downloads.append(info[key]['realInstalls'])


sorted_indices = numpy.argsort(percentage)

percentage=numpy.array(percentage)[sorted_indices]
downloads=numpy.array(downloads)[sorted_indices]

plt.figure(figsize=(8, 6))  # Adjust width and height as needed

# Create a basic line plot
plt.scatter(downloads, percentage, label='Data Points', color='blue', marker='o',s=5)

# Add labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Dot Diagram')

plt.ylim(0, 0.2)  # Adjust the limits as needed
plt.xlim(0, 10000000)  # Adjust the limits as needed

# Add a legend (if needed)
plt.legend()

# Display the plot
plt.savefig('scatter_plot.png')

# Display the plot (optional)
plt.show()
