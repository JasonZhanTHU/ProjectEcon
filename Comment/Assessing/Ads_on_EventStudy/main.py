from Gather_Ads import gather_ads
from Gather_Ads_Estimates import gather_ads_estimates
import pandas as pd
from datetime import *
import json
import matplotlib.pyplot as plt

date_format = "%Y-%m-%d"

with open('setup.json', 'r') as f:
    spec = json.load(f)
with open('period.json', 'r') as f:
    period = json.load(f)

ads, info = gather_ads(spec)


def get_data(spec, period):
    ad_estimate, ad_actual = gather_ads_estimates(spec, period, ads, info)
    return ad_estimate, ad_actual


l1 = []
l2 = []
x_axis = []

tot_estimate=0
tot_actual=0

for i in range(0, 100):
    ad_estimate, ad_actual = get_data(spec, period)

    if period['predict_start']>=period['count_period_start'] and period['predict_end']<=period['count_period_end']:
        tot_estimate+=ad_estimate
        tot_actual+=ad_actual


    l1.append(ad_estimate)
    l2.append(ad_actual)
    print("P", i, " has predict value ", ad_estimate, " and actual value", ad_actual)

    period['predict_start'] = pd.to_datetime(period['predict_start']) + pd.DateOffset(days=7)
    period['predict_start'] = str(period['predict_start'])[:10]

    period['predict_end'] = pd.to_datetime(period['predict_end']) + pd.DateOffset(days=7)
    period['predict_end'] = str(period['predict_end'])[:10]
    x_axis.append(period['predict_start'])

plt.figure(figsize=(25, 15))

plt.plot(x_axis, l1, label='Predicted Negative Ad Reviews', marker='o', linestyle='-')
plt.plot(x_axis, l2, label='Actual Negative Ad Reviews', marker='o', linestyle='-')


def add_verticle(str, label):
    for x in x_axis:
        if str<x:
            plt.axvline(x=x, color='red', linestyle='--', label=label)
            return

add_verticle('2016-04-14', 'GDPR Announced')
add_verticle('2018-05-25', 'GDPR Implemented')

showed = []
for i in range(0, len(x_axis), 25):
    showed.append(x_axis[i])

plt.xticks(showed)
plt.xlabel('Week')
plt.ylabel('Negative Comment on Ads Count')
plt.legend()
plt.grid(True)
plt.show(block=True)


print((tot_actual-tot_estimate)/tot_estimate)
