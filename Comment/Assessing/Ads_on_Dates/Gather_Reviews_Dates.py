import json
import os
import re
from tqdm import tqdm


def gather_reviews_dates(spec):
    folder_path = os.path.expanduser("~/Downloads/all_reviews")

    file_names = os.listdir(folder_path)

    with open('../../files/all_App_info.json', 'r') as f:
        app_data = json.load(f)

    data = {}

    for file_name in tqdm(file_names, desc="Processing items"):
        file_path = os.path.join(folder_path, file_name)

        if not file_name in app_data:
            continue
        if file_name in spec['skip']:
            continue
        if spec['region'] !=[] and not app_data[file_name]['region'] in spec['region']:
            continue
        if spec['developer'] !=[] and app_data[file_name]['developer'] not in spec['developer']:
            continue
        if app_data[file_name]['realInstalls'] < spec['min_download']:
            continue
        if app_data[file_name]['realInstalls'] > spec['max_download']:
            continue
        if app_data[file_name]['released'] is None or app_data[file_name]['released'] > spec['latest_release'] or \
                app_data[file_name]['released'] < spec['earliest_release']:
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reviews = json.load(f)
            for review in reviews:
                if review['date'][:10] not in data:
                    data[review['date'][:10]] = 0
                data[review['date'][:10]] += 1

        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading JSON from '{file_path}': {e}")

    data = sorted(data.items())
    data = dict(data)

    return data
