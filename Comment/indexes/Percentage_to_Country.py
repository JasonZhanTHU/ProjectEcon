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


def check_distribution(array1, array2, array3, array4, array5):
    # 执行KS检验比较所有数组两两之间的分布
    arrays = [array1, array2, array3, array4, array5]
    p_values = numpy.zeros((5, 5))

    for i in range(5):
        for j in range(5):
            if i != j:
                statistic, p_value = stats.ks_2samp(arrays[i], arrays[j])
                p_values[i][j] = "{:.2f}".format(p_value)
            else:
                p_values[i][j] = -1
    return p_values.tolist()


data = {}
for key in info:
    if info[key]['region'] not in data:
        data[info[key]['region']] = []
    cur=info[key]['ad_complaints']/info[key]['review_sum']
    data[info[key]['region']].append(cur)


res=check_distribution(data['Europe'], data['Oceania'], data['Asia'], data['Africa'], data['Americas'])

fig, ax = plt.subplots()

# Hide axes
ax.axis('off')

res.insert(0, ['Europe', 'Oceania', 'Asia','Africa','Americas'])
res[0].insert(0, '')
res[1].insert(0, 'Europe')
res[2].insert(0, 'Oceania')
res[3].insert(0, 'Asia')
res[4].insert(0, 'Africa')
res[5].insert(0, 'Americas')

# Create the table
table = ax.table(cellText=res, loc='center', cellLoc='center')

column_labels = ['Europe', 'Oceania', 'Asia','Africa','Americas']

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)  # 控制提示栏的高度

# 设置表格的纵向提示栏

# 隐藏坐标轴
ax.axis('off')

# 显示图表
plt.show()