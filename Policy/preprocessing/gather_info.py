import pandas
import json
import ast
import os

folder_path = os.path.expanduser("~/Downloads/all_infos")
#folder_path = os.path.expanduser("main4.py")


# 使用os.listdir()获取文件夹内所有文件和子文件夹的列表
file_names = os.listdir(folder_path)


#file_names=['com.instantcardchange.app']

data_lists=[]

# 打印所有文件名
for file_name in file_names:
    file_path=os.path.join(folder_path,file_name)


    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            data = json.loads(content)
            print('done')

            data['app_identifier']=file_name

            data_lists.append(data)

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading JSON from '{file_path}': {e}")

df = pandas.DataFrame(data_lists)

print(df)

df.to_csv('all_info.csv')
