import os

folder_path = os.path.expanduser("~/Downloads/all_infos")
file_names = os.listdir(folder_path)

for file_name in file_names:
    input_file_path = os.path.join(folder_path, file_name)
    output_file_path = os.path.join(folder_path, file_name)

    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

    # 将单引号替换为双引号
    content = content.replace("\"", "'")


    content = content.replace(": '", ": \"")
    content = content.replace("',", "\",")

    content = content.replace("{'", "{\"")
    content = content.replace("':", "\":")
    content = content.replace(", '", ", \"")
    content = content.replace("'}", "\"}")
    content = content.replace("']", "\"]")
    content = content.replace("['", "[\"")

    content = content.replace("\\r", " ")
    content = content.replace("\\n", " ")

    content = content.replace("\\", "")

    content = content.replace("None", "null")
    content = content.replace("True", "true")
    content = content.replace("False", "false")

    # 将处理后的内容保存到新文件中
    with open(output_file_path, 'w') as output_file:
        output_file.write(content)

    print(f"Processed and saved: {output_file_path}")
