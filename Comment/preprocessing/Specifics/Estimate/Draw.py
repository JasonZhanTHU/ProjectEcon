import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import gaussian_kde

# Simulated distribution data (replace with your actual data)
np.random.seed(0)
with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/Specifics/Estimate_Ads.json', 'r') as f:
    data = json.load(f)

x = np.linspace(1, 1800, 1800)
data = np.array(data[:1800])

# 使用Savitzky-Golay 滤波器后得到平滑图线
from scipy.signal import savgol_filter

y = savgol_filter(data, 14, 2, mode= 'nearest')


y/=y.sum()
plt.plot(x, y*100, 'b', label = 'savgol')

cdf=[]
cdf.append(y[0])
for i in range(1,len(y)):
    cdf.append(cdf[i-1]+y[i])
#plt.plot(x, cdf, 'b', label = 'savgol')

plt.xlabel('Days after first comment')
plt.ylabel('Percentage of negative ad comment released')

plt.show()

with open('../../../files/Specifics/Estimate_Ads_CDF.json', 'w') as json_file:
    json.dump(cdf, json_file, indent=4)
