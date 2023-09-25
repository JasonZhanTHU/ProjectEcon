import json
from datetime import *
import pandas as pd

date_format = "%Y-%m-%d"


def gather_ads_estimates(spec, period, data, info):

    with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/Specifics/Estimate_Ads_CDF.json', 'r') as f:
        cdf = json.load(f)

    predict = 0
    actual = 0

    for key in data:

        if not key in info:
            continue

        if not 'earliest_comment' in info[key]:
            continue

        if key >= "com.panotogomo.nuclear":
            continue
        additional_limit = str(
            pd.to_datetime(period['predict_end']) - pd.DateOffset(days=period['maximum_estimation']))
        if info[key]['earliest_comment'] < additional_limit:
            continue

        if info[key]['earliest_comment'] > str(pd.to_datetime(period['interval_end'])):
            continue

        sample = 0

        for index in data[key]:
            if not data[key][index]['sentiment'] in spec['sentiment']:
                continue

            comment_datetime = data[key][index]['date'][:10]

            if comment_datetime > period['interval_start'] and comment_datetime <= period['interval_end']:
                sample += 1

            if comment_datetime > period['predict_start'] and comment_datetime <= period['predict_end']:
                actual += 1

        sample_window_start = (datetime.strptime(period['interval_start'], date_format) - datetime.strptime(
            info[key]['earliest_comment'][:10], date_format)).days
        if sample_window_start < 0:
            sample_window_start = -1

        sample_window_end = (datetime.strptime(period['interval_end'], date_format) - datetime.strptime(
            info[key]['earliest_comment'][:10], date_format)).days

        predict_window_end = (datetime.strptime(period['predict_end'], date_format) - datetime.strptime(
            info[key]['earliest_comment'][:10], date_format)).days

        predict_window_start = (datetime.strptime(period['predict_start'], date_format) - datetime.strptime(
            info[key]['earliest_comment'][:10], date_format)).days

        try:
            cur_predict = (cdf[predict_window_end] - cdf[predict_window_start]) / (
                    cdf[sample_window_end] - (cdf[sample_window_start] if sample_window_start > -1 else 0)) * sample
        except Exception as e:
            print(predict_window_end)
            print(sample_window_end)
            # print(f"An error occurred: {e}")

        predict += cur_predict

    return predict, actual
