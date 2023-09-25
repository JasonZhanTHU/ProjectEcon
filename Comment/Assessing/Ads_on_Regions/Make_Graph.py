from Gather_Ads import gather_ads
from Gather_Ads_Dates import gather_ads_dates
from Gather_Reviews_Dates import gather_reviews_dates
from Create_Graph import create_graph
import matplotlib.pyplot as plt
import json

with open('setup.json', 'r') as f:
    specs = json.load(f)
with open('period.json', 'r') as f:
    period = json.load(f)


def get_data(spec, mode):
    ads, info = gather_ads(spec)
    ad_calendar = gather_ads_dates(spec, ads, info, mode)
    if mode == 'percentage':
        reviews_calendar = gather_reviews_dates(spec)
        res = create_graph(period, ad_calendar, reviews_calendar)
    else:
        res = create_graph(period, ad_calendar)

    return res


plt.figure(figsize=(25, 15))
x_axis = list(range(-period['prev_days'], period['latt_days'] + 1, period['slide']))

for key in specs:
    data = get_data(specs[key], period['mode'])
    plt.plot(x_axis, data, label=key, marker='o', linestyle='-')

plt.axvline(x=0, color='red', linestyle='--', label='Event Date')
plt.axvline(x=730, color='red', linestyle='--', label='Event Date')
plt.xlabel(period['xlable'])
plt.ylabel(period['ylable'])
plt.legend()
plt.grid(True)
plt.show(block=True)
