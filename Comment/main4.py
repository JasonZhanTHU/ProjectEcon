import os
import platform
import random
import signal
from transformers import AutoTokenizer, AutoModel
import readline
import json

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().quantize(8).cuda()
model = model.eval()

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'
stop_stream = False


def build_prompt(history):
    prompt = ""
    for query, response in history:
        prompt += f"{response}"
    return prompt


def signal_handler(signal, frame):
    global stop_stream
    stop_stream = True


def main():
    with open('questions_reviews.json', 'r') as input_file:
        content = json.load(input_file)

    all_response = {}

    history = []
    global stop_stream
    print("欢迎使用 ChatGLM-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")

    for key in content:

        cur_response = {}
        for item in content[key]:
            query = content[key][item]
            if len(query) > 40000:
                continue
            if query.strip() == "stop" or random.randint(0, 100) % 10 == 0:
                break
            if query.strip() == "clear":
                history = []
                continue
            query = '"' + query
            query += '"Is this comment positive on ads or negative. Answer with a word."'
            count = 0
            for response, history in model.stream_chat(tokenizer, query, history=history):
                if stop_stream:
                    stop_stream = False
                    break
            res = build_prompt(history)
            # print(res, flush=True)
            print(key, "::", item)

            cur_response[item] = res
        all_response[key] = cur_response

    json_filename = 'response3.json'
    with open(json_filename, 'w') as json_file:
        json.dump(all_response, json_file, indent=4)


if __name__ == "__main__":
    main()
