
import re
import json

#operating_file = 'Premium_Ads.json'
operating_file = 'Premium_Ads.json'


def do_query(str):
    print(str)

def is_substring(substring, main_string):
    return main_string.find(substring) != -1


def process(str):
    result = re.split(r'[.!?]|but|except', str)
    res = ""
    for s in result:
        if (is_substring('ads', s) or is_substring('Ads', s)):
            res += s + '.'
    return res

if __name__ == "__main__":
    with open(operating_file, 'r') as input_file:
        content = json.load(input_file)

    count=0

    for key in content:
        cur_response = {}
        for item in content[key]:
            count+=1
            query = content[key][item]

            do_query('"' + query['review'] + '"Does this comment mention the author having paid for the game.')

            #print(count)