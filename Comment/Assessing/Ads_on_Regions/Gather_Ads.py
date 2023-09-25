import json
import os
import re


def gather_ads(spec):
    with open('../../files/ad_reviews.json', 'r') as f:
        data = json.load(f)

    with open('../../files/all_App_info.json', 'r') as f:
        app_data = json.load(f)

    result = {}
    info = {}

    for file_name in data:
        if not file_name in app_data:
            continue
        if spec['developer'] !=[] and app_data[file_name]['developer'] not in spec['developer']:
            continue
        if file_name in spec['skip']:
            continue
        if spec['region'] !=[] and not app_data[file_name]['region'] in spec['region']:
            continue
        if app_data[file_name]['realInstalls'] < spec['min_download']:
            continue
        if app_data[file_name]['realInstalls'] > spec['max_download']:
            continue
        if app_data[file_name]['released'] is None or app_data[file_name]['released'] > spec['latest_release'] or \
                app_data[file_name]['released'] < spec['earliest_release']:
            continue
        result[file_name] = data[file_name]
        info[file_name] = app_data[file_name]

    print("Considering ", len(result), " cases")

    return result, info
