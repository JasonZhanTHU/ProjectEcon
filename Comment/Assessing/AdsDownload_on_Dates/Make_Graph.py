from Gather_Ads import gather_ads
from Gather_Ads_Dates import gather_ads_dates
from Create_Graph import create_graph
import matplotlib.pyplot as plt

period = {
    'event_date': '2016-05-24',
    'prev_days': 365*2,
    'latt_days': 365*2,
}


def get_data(spec):
    ads=gather_ads(spec)
    ad_calendar=gather_ads_dates(spec,ads)
    res = create_graph(period, ad_calendar)
    return res


l1 = None
l2 = None
l3 = None
l4 = None
l5 = None
l6 = None

spec = {
    'region': ['Europe'],
    'min_download': -1,
    'max_download': 10000000000,
    'earliest_release': '1000',
    'latest_release': '2018-05-25',
    'sentiment': ['NEGATIVE']
}
l1 = get_data(spec)

plt.figure(figsize=(25, 15))
x_axis = list(range(-period['prev_days'], period['latt_days'] + 1))
if l1 is not None:
    plt.plot(x_axis, l1, label='EU', marker='o', linestyle='-')
if l2 is not None:
    plt.plot(x_axis, l2, label='OCEANIA', marker='o', linestyle='-')
if l3 is not None:
    plt.plot(x_axis, l3, label='AFRICA', marker='o', linestyle='-')
if l4 is not None:
    plt.plot(x_axis, l4, label='ASIA', marker='o', linestyle='-')
if l5 is not None:
    plt.plot(x_axis, l5, label='AMERICAS', marker='o', linestyle='-')
if l6 is not None:
    plt.plot(x_axis, l6, label='AVERAGE', marker='o', linestyle='-')

plt.axvline(x=0, color='red', linestyle='--', label='Event Date')
plt.xlabel('Days Relative to GDPR')
plt.ylabel('Ad-related Comments Percentage')
plt.legend()
plt.grid(True)
plt.show(block=True)
