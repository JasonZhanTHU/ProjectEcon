import json

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/compressed.json', 'r') as f:
    data = json.load(f)

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'r') as f:
    app_data = json.load(f)

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/calendar.json', 'r') as f:
    calendar = json.load(f)


def check_validity(file, spec):
    if file not in app_data:
        return False
    if spec['developer'] != [] and app_data[file]['developer'] not in spec['developer']:
        return False
    if file in spec['skip']:
        return False
    if spec['region'] != [] and not app_data[file]['region'] in spec['region']:
        return False
    if spec['latest_earliest_comment'] is not None and (
            'earliest_comment' not in app_data[file] or app_data[file]['earliest_comment'] > spec[
        'latest_earliest_comment']):
        return False
    if app_data[file]['realInstalls'] < spec['min_download']:
        return False
    if app_data[file]['realInstalls'] > spec['max_download']:
        return False
    if app_data[file]['released'] is None or app_data[file]['released'] > spec['latest_release'] or \
            app_data[file]['released'] < spec['earliest_release']:
        return False
    return True


def gather_comments(spec):
    result = {}
    tmp = {}
    info = {}

    for day in calendar:
        result[day] = 0
        tmp[day] = 0

    for file in data:
        if not check_validity(file, spec):
            continue

        if 'POSITIVE' in spec['sentiment']:
            for day in data[file]['Positive']:
                result[day] += data[file]['Positive'][day]

        if 'NEGATIVE' in spec['sentiment']:
            for day in data[file]['Negative']:
                result[day] += data[file]['Negative'][day]

        for day in data[file]['Positive']:
            tmp[day] += data[file]['Positive'][day]
        for day in data[file]['Negative']:
            tmp[day] += data[file]['Negative'][day]

    for day in result:
        if tmp[day]==0:
            result[day]=0
        else:
            result[day]/=tmp[day]

    return result, info
