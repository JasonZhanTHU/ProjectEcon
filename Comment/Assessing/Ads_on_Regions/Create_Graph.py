import pandas as pd
import json


def create_graph(spec, ad_calendar, reviews_calendar=None):
    with open('../../files/calendar.json', 'r') as f:
        calendar = json.load(f)
    if reviews_calendar is None:
        reviews_calendar={}

    for key in calendar:
        if key not in ad_calendar:
            ad_calendar[key] = 0
        if key not in reviews_calendar:
            reviews_calendar[key] = 0

    dates = []
    ads = []
    reviews = []
    for key in reviews_calendar:
        dates.append(key)
        ads.append(ad_calendar[key])
        reviews.append(reviews_calendar[key])

    data = {'date': dates,
            'ads': ads,
            'reviews': reviews}

    data = pd.DataFrame(data)

    event_date = spec['event_date']
    event_window_before = spec['prev_days']
    event_window_after = spec['latt_days']

    # 4. 计算事件期间的超额收益率
    # 创建一个列表来存储每个时期的超额收益率
    returns = []

    for i in range(-event_window_before, event_window_after + 1, spec['slide']):
        window_start = pd.to_datetime(event_date) + pd.DateOffset(days=i)
        window_end = window_start + pd.DateOffset(days=spec['window'])
        window_start = str(window_start)
        window_end = str(window_end)

        event_window = data[(data['date'] >= window_start) & (data['date'] < window_end)]

        if spec['mode'] == "percentage":
            average_return_event = event_window['ads'].mean() / event_window['reviews'].mean()
        elif spec['mode'] == 'count' or spec['mode'] == 'app' or spec['mode'] == 'corp':
            average_return_event = event_window['ads'].mean()
        else:
            average_return_event = 0

        returns.append(average_return_event)

    return returns
