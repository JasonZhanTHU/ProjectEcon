from Gather_Ads import gather_ads
from Gather_Ads_Dates import gather_ads_dates
from Gather_Reviews_Dates import gather_reviews_dates
from Merge_Statistics import merge_statistics
import json
import numpy as np

with open('setup.json', 'r') as f:
    spec = json.load(f)
with open('period.json', 'r') as f:
    periods = json.load(f)


def get_data(spec):
    ads, info = gather_ads(spec)
    ad_calendar = gather_ads_dates(spec, ads, info, spec['mode'])
    if spec['mode'] == 'percentage':
        reviews_calendar = gather_reviews_dates(spec)
    else:
        reviews_calendar = None
    return ad_calendar, reviews_calendar


def solve(period, ad_calendar, reviews_calendar, mode):
    if mode == 'percentage':
        res = merge_statistics(period, ad_calendar, reviews_calendar)
    else:
        res = merge_statistics(period, ad_calendar)

    mean_value = np.mean(res)
    std_deviation = np.std(res)

    return mean_value, std_deviation


ad_calendar, reviews_calendar = get_data(spec)

for key in periods:
    mean, dev = solve(periods[key], ad_calendar, reviews_calendar, spec['mode'])
    print(key, " has mean value ", mean, " and standard derivation", dev)
