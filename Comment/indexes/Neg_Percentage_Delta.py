import pandas as pd
import matplotlib.pyplot as plt
import json


with open('../files/ad_reviews_date.json', 'r') as f:
    ad = json.load(f)

with open('../files/ad_EU_reviews_date.json', 'r') as f:
    ad_EU = json.load(f)

with open('../files/all_reviews_date.json', 'r') as f:
    all = json.load(f)

with open('../files/all_EU_reviews_date.json', 'r') as f:
    all_EU = json.load(f)

for key in all:
    if key not in ad:
        ad[key] = 0  # or any default value you prefer
    if key not in ad_EU:
        ad_EU[key] = 0  # or any default value you prefer
    if key not in all_EU:
        all_EU[key] = 0  # or any default value you prefer

dates = []
ads = []
alls = []
ads_EU = []
alls_EU = []
for key in ad:
    dates.append(key)
    ads.append(ad[key])
    alls.append(all[key])
    ads_EU.append(ad_EU[key])
    alls_EU.append(all_EU[key])
    ad[key]-=ad_EU[key]


data = {'date': dates,
        'ad': ads,
        'all': alls,
        'ad_EU': ads_EU,
        'all_EU': alls_EU}

data = pd.DataFrame(data)

# 3. 定义事件窗口
# 事件窗口是一个用于分析事件影响的时间段，通常包括事件前期、事件当日和事件后期
event_date = '2018-05-25'  # 替换为事件日期
event_window_before = 1000  # 事件前期天数
event_window_after = 1000  # 事件后期天数

# 4. 计算事件期间的超额收益率
# 创建一个列表来存储每个时期的超额收益率
excess_returns = []
excess_returns1 = []
excess_returns2 = []

for i in range(-event_window_before, event_window_after + 1):
    window_start = pd.to_datetime(event_date) + pd.DateOffset(days=i)
    window_end = window_start + pd.DateOffset(days=7)
    window_start = str(window_start)
    window_end = str(window_end)

    event_window = data[(data['date'] >= window_start) & (data['date'] < window_end)]
    market_window = data[(data['date'] >= window_start) & (data['date'] < window_end)]

    average_return_event = event_window['ad_EU'].mean() / event_window['all_EU'].mean()
    average_return_market = (event_window['ad'].mean()-event_window['ad_EU'].mean()) / (event_window['all'].mean()-event_window['all_EU'].mean())

    print(event_window['ad_EU'].mean()-event_window['ad'].mean())
    excess_return = average_return_event - average_return_market
    excess_returns.append(excess_return)  # 将超额收益转换为百分比
    excess_returns1.append(average_return_event)  # 将超额收益转换为百分比
    excess_returns2.append(average_return_market)  # 将超额收益转换为百分比

# 5. 可视化超额收益曲线
plt.figure(figsize=(10, 6))
x_axis = list(range(-event_window_before, event_window_after + 1))
plt.plot(x_axis, excess_returns, marker='o', linestyle='-')
plt.axvline(x=0, color='red', linestyle='--', label='Event Date')
plt.title('EU and Elsewhere Ad comment percentage')
plt.xlabel('Days Relative to GDPR')
plt.ylabel('Delta in Ad-related Comments Percentage')
plt.legend()
plt.grid(True)
plt.show()
