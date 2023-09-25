import json
import os


current_directory = os.getcwd()
print(current_directory)

with open('../files/all_response.json', 'r') as input_file:
    content = json.load(input_file)


questions={}
count=0
for key in content:

    count+=1
    questions[count]=content[key]
    print(len(questions[count]))
    count+=1
    questions[count]='clear'


json_filename = '../files/questions2.json'
with open(json_filename, 'w') as json_file:
    json.dump(questions, json_file, indent=4)