import os
import platform
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
    prompt=""
    for query, response in history:
        prompt += f"{response}"
    return prompt


def signal_handler(signal, frame):
    global stop_stream
    stop_stream = True


def main():
    with open('questions.json', 'r') as input_file:
        content = json.load(input_file)

    all_response = {}

    history = []
    global stop_stream
    print("欢迎使用 ChatGLM-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")

    with open('all_response.json', 'r') as result_file:
        result = json.load(result_file)

    for key in content:

        if key in result:
            continue

        query = content[key]
        if len(query) > 40000:
            continue
        if query.strip() == "stop":
            break
        if query.strip() == "clear":
            history = []
            os.system(clear_command)
            print("欢迎使用 ChatGLM-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
            continue
        count = 0
        for response, history in model.stream_chat(tokenizer, query, history=history):
            if stop_stream:
                stop_stream = False
                break
            else:
                count += 1
                if count % 8 == 0:
                    os.system(clear_command)
                    print(build_prompt(history), flush=True)
                    signal.signal(signal.SIGINT, signal_handler)
        os.system(clear_command)
        res = build_prompt(history)
        print(res, flush=True)

        all_response[int(int(key) / 2)] = res

    json_filename = 'files/response1.json'
    with open(json_filename, 'w') as json_file:
        json.dump(all_response, json_file, indent=4)


if __name__ == "__main__":
    main()

