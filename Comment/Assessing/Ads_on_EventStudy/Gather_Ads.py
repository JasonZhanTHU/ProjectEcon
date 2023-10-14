import json

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/ad_reviews.json', 'r') as f:
    data = json.load(f)

with open('/Users/jasonzhan/Downloads/ProjectEcon_ExternalFiles/all_App_info.json', 'r') as f:
    app_data = json.load(f)


def check_validity(file, spec):
    if file not in app_data:
        return False
    if spec['developer'] != [] and app_data[file]['developer'] not in spec['developer']:
        return False
    if file in spec['skip']:
        return False
    if spec['region'] != [] and not app_data[file]['region'] in spec['region']:
        return False
    if spec['genre'] != [] and not app_data[file]['genre'] in spec['genre']:
        return False
    if app_data[file]['price'] > spec['max_price'] or app_data[file]['price'] < spec['min_price']:
        return False
    if spec['latest_earliest_release'] is not None and ('earliest_comment' not in app_data[file] or app_data[file]['earliest_comment'] > spec['latest_earliest_release']):
        return False
    if app_data[file]['realInstalls'] < spec['min_download']:
        return False
    if app_data[file]['realInstalls'] > spec['max_download']:
        return False
    if app_data[file]['released'] is None or app_data[file]['released'] > spec['latest_release'] or \
            app_data[file]['released'] < spec['earliest_release']:
        return False
    return True


def gather_ads(spec):
    result = {}
    info = {}

    for file in data:
        if check_validity(file, spec) == False:
            continue
        result[file] = data[file]
        info[file] = app_data[file]

    print("Considering ", len(result), " cases")

    return result, info
