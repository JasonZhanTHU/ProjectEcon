import json

def gather_ads_dates(spec, data):

    calendar = {}

    for key in data:
        for index in data[key]:
            # print(data[key][index]['sentiment'])
            if not data[key][index]['sentiment'] in spec['sentiment']:
                continue
            if data[key][index]['date'][:10] not in calendar:
                calendar[data[key][index]['date'][:10]] = 0
            calendar[data[key][index]['date'][:10]] += 1
    return calendar
