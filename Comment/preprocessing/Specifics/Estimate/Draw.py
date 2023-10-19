import json
import numpy as np
import matplotlib.pyplot as plt
from Est_Comment import operate


#operate(['Tools', 'Libraries & Demo', 'Travel & Local', 'Productivity', 'Communication', 'Maps & Navigation', 'Weather'])
#operate(['Action', 'Music & Audio', 'Video Players & Editors', 'Personalization', 'Puzzle', 'Board', 'Casual', 'Sports', 'Simulation', 'Role Playing', 'Arcade', 'Card', 'Adventure', 'Trivia', 'Casino'])
# operate(['Health & Fitness', 'Food & Drink', 'House & Home', 'Beauty', 'Parenting'])
# operate(['Entertainment', 'Music', 'Photography', 'Movies & TV Shows'])
#operate(['Education', 'Books & Reference', 'News & Magazines'])
#operate(['Shopping', 'Business', 'Finance'])
operate([])

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/Specifics/Estimate_Count.json', 'r') as f:
    data = json.load(f)

x = np.linspace(1, 900, 900)
data = np.array(data[:900])

# 使用Savitzky-Golay 滤波器后得到平滑图线
# from scipy.signal import savgol_filter

# y = savgol_filter(data, 14, 2, mode= 'nearest')


y=data
y/=y.sum()
plt.plot(x, y*100, 'b', label = 'savgol')

cdf=[]
cdf.append(y[0])
for i in range(1,len(y)):
    cdf.append(cdf[i-1]+y[i])

plt.xlabel('Days after first comment')
plt.ylabel('Percentage of negative ad comment released')

plt.show()

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/Specifics/Estimate_CDF.json', 'w') as json_file:
    json.dump(cdf, json_file, indent=4)
