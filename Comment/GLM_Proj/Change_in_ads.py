import os
import platform
import random
import signal
from transformers import AutoTokenizer, AutoModel
import readline
import json
import random

operating_file = 'Premium_Ads.json'
result_file = 'response.json'

tokenizer = AutoTokenizer.from_pretrained("../autodl-tmp/ChatGLM", trust_remote_code=True)
model = AutoModel.from_pretrained("../autodl-tmp/ChatGLM", trust_remote_code=True).half().cuda()
model = model.eval()

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'


def is_substring(substring, main_string):
    return main_string.find(substring) != -1


def process(str):
    result = re.split(r'[.!?]|but|except', str)
    res = ""
    for s in result:
        if (is_substring('ads', s) or is_substring('Ads', s)):
            res += s + '.'
    return res


def do_query(str):
    response, history = model.chat(tokenizer, str, history=[])
    return response


if __name__ == "__main__":
    with open(operating_file, 'r') as input_file:
        content = json.load(input_file)

    print("欢迎使用 ChatGLM-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")

    count = 0
    for key in content:
        cur_response = {}
        for item in content[key]:
            query = content[key][item]

            result = do_query('"' + query['review'] + '"Does this comment mention the author having paid for the game. Answer only Yes or No."')
            content[key][item]['paid'] = 1 if is_substring('Yes', result) else 0
            count += 1
            print(count)

            if count%1000==0:
                json_filename = 'Processed1.json'
                with open(json_filename, 'w') as json_file:
                    json.dump(content, json_file, indent=4)
    json_filename = 'Processed1.json'
    with open(json_filename, 'w') as json_file:
        json.dump(content, json_file, indent=4)