import os
import json

def update_json_files(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为JSON文件
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            # 读取JSON文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            # 更新status项为1
            update_status(data)
            # 写入更新后的内容回到文件中
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

def update_status(data):
    # 遍历JSON数据中的各项，更新status为1
    for key, value in data.items():
        if isinstance(value, dict) and 'status' in value:
            value['status'] = 0
        elif isinstance(value, dict):
            update_status(value)

# 用于存放JSON文件的文件夹路径
folder_path = 'conf'
# 调用函数更新JSON文件中的status项
update_json_files(folder_path)
