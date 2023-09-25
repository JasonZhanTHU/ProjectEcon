import json


def gather_ads_dates(spec, data, info, mode="percentage"):
    calendar = {}
    rem = {}

    for key in data:
        for index in data[key]:
            # print(data[key][index]['sentiment'])
            if not data[key][index]['sentiment'] in spec['sentiment']:
                continue
            if mode == "percentage" or mode == "count":
                if data[key][index]['date'][:10] not in calendar:
                    calendar[data[key][index]['date'][:10]] = 0
                calendar[data[key][index]['date'][:10]] += 1

            if mode == "app":
                if data[key][index]['date'][:10] not in calendar:
                    calendar[data[key][index]['date'][:10]] = 0
                    rem[data[key][index]['date'][:10]] = {}

                if key not in rem[data[key][index]['date'][:10]]:
                    calendar[data[key][index]['date'][:10]] += 1
                    rem[data[key][index]['date'][:10]][key] = 1

            if mode == "corp":
                if data[key][index]['date'][:10] not in calendar:
                    calendar[data[key][index]['date'][:10]] = 0
                    rem[data[key][index]['date'][:10]] = {}

                if info[key]['developer'] not in rem[data[key][index]['date'][:10]]:
                    calendar[data[key][index]['date'][:10]] += 1
                    rem[data[key][index]['date'][:10]][info[key]['developer']] = 1

    return calendar
