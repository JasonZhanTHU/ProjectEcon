import pandas as pd
import json


def merge_statistics(period, ad_calendar, reviews_calendar=None):
    data = []

    for key in ad_calendar:
        if key >= period['start_date'] and key <= period['end_date']:
            if reviews_calendar is None:
                data.append(ad_calendar[key])
            else:
                data.append(ad_calendar[key] / reviews_calendar[key])

    return data
