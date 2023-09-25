import json
import numpy
from scipy import stats
import matplotlib.pyplot as plt





with open('../files/all_App_info.json', 'r') as f:
    info = json.load(f)

with open('../files/ad_reviews.json', 'r') as f:
    ad = json.load(f)

with open('../files/corp_reviews.json', 'r') as f:
    all = json.load(f)

percentage = []
individual = []

per1 = []
tot1 = 0
per2 = []
tot2 = 0
for key in info:
    if info[key]['individual'] == 1:
        per1.append(info[key]['ad_complaints'] / info[key]['review_sum'])


    else:
        per2.append(info[key]['ad_complaints'] / info[key]['review_sum'])


per1 = numpy.array(per1)
per2 = numpy.array(per2)

mean_value1 = numpy.mean(per1)

# Calculate the square of the array
var_value1 = numpy.var(per1)

# Print the results
print("Mean For individual", mean_value1)
print("Squared Array For individual", var_value1)

print("\n\n")
mean_value2 = numpy.mean(per2)

# Calculate the square of the array
var_value2 = numpy.var(per2)

# Print the results
print("Mean For corperation", mean_value2)
print("Squared Array For corperation", var_value2)

statistic, p_value = stats.ks_2samp(per1, per2)

# 打印KS检验的结果
print("KS检验统计量:", statistic)
print("p-value:", p_value)

# 设置显著性水平（通常为0.05）
alpha = 0.05

# 根据p-value和显著性水平进行假设检验
if p_value > alpha:
    print("无法拒绝原假设：两个数组来自相同的分布")
else:
    print("拒绝原假设：两个数组来自不同的分布")
