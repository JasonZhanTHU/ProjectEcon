import json
from datetime import *
import pandas as pd

date_format = "%Y-%m-%d"


def gather_comments_estimates(spec, period, data, info):

    with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/Specifics/Estimate_CDF.json', 'r') as f:
        cdf = json.load(f)

    predict = 0
    actual = 0

    for key in data:

        if not key in info:
            continue

        if info[key]['released'] is None:
            continue
        additional_limit = str(
            pd.to_datetime(period['predict_end']) - pd.DateOffset(days=period['maximum_estimation']))

        if info[key]['released'] < additional_limit:
            continue

        if info[key]['released'] > str(pd.to_datetime(period['interval_end'])):
            continue

        sample = 0
        cur=0
        for index in data[key]:
            for cmt in data[key][index]:
                comment_datetime = cmt[:10]

                if comment_datetime > period['interval_start'] and comment_datetime <= period['interval_end']:
                    sample += data[key][index][cmt]

                if comment_datetime > period['predict_start'] and comment_datetime <= period['predict_end']:
                    cur += data[key][index][cmt]

        sample_window_start = (datetime.strptime(period['interval_start'], date_format) - datetime.strptime(
            info[key]['released'][:10], date_format)).days
        if sample_window_start < 0:
            sample_window_start = -1

        sample_window_end = (datetime.strptime(period['interval_end'], date_format) - datetime.strptime(
            info[key]['released'][:10], date_format)).days

        predict_window_end = (datetime.strptime(period['predict_end'], date_format) - datetime.strptime(
            info[key]['released'][:10], date_format)).days

        predict_window_start = (datetime.strptime(period['predict_start'], date_format) - datetime.strptime(
            info[key]['released'][:10], date_format)).days

        try:
            cur_predict = (cdf[predict_window_end] - cdf[predict_window_start]) / (
                    cdf[sample_window_end] - (cdf[sample_window_start] if sample_window_start > -1 else 0)) * sample
            predict += cur_predict
            actual += cur
        except Exception as e:
            print(predict_window_end)
            print(sample_window_end)
            print(f"An error occurred: {e}")




    return predict, actual
