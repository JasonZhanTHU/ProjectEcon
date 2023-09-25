import pandas as pd
import json


def create_graph(spec, ad_calendar):
    with open('../../files/Specifics/Estimate_Downloads_EU.json', 'r') as f:
        calendar = json.load(f)

    for key in calendar:
        if key not in ad_calendar:
            ad_calendar[key] = 0

    dates = []
    ads = []
    downloads = []
    for key in calendar:
        dates.append(key)
        ads.append(ad_calendar[key])
        downloads.append(calendar[key])

    data = {'date': dates,
            'ads': ads,
            'downloads': downloads}

    data = pd.DataFrame(data)

    event_date = spec['event_date']
    event_window_before = spec['prev_days']
    event_window_after = spec['latt_days']

    # 4. 计算事件期间的超额收益率
    # 创建一个列表来存储每个时期的超额收益率
    returns = []

    for i in range(-event_window_before, event_window_after + 1):
        window_start = pd.to_datetime(event_date) + pd.DateOffset(days=i)
        window_end = window_start + pd.DateOffset(days=7)
        window_start = str(window_start)
        window_end = str(window_end)

        window_start2 = pd.to_datetime(event_date) + pd.DateOffset(days=i + 7)
        window_end2 = window_start2 + pd.DateOffset(days=7)
        window_start2 = str(window_start2)
        window_end2 = str(window_end2)

        event_window = data[(data['date'] >= window_start) & (data['date'] < window_end)]
        event_window2 = data[(data['date'] >= window_start2) & (data['date'] < window_end2)]

        average_return_event = event_window['ads'].mean() / event_window2['downloads'].mean()

        returns.append(average_return_event)

    return returns
