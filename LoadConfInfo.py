import json
import os
from typing import List, Any
import csv
import xmlContent
import xmlMatch
from rapidfuzz.process import extractOne
import time

def get_filepath_list(directory: str) -> List[str]:
    """
    获取目录下的所有带路径的 json 文件名，并以列表形式返回
    :param directory:
    :return: filepath_list 返回目录下所有JSON文件的路径
    """
    filepath_list = []
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            # 拼接获取JSON文件的相对路径
            filepath = os.path.join(directory, filename)
            filepath_list.append(filepath)
    return filepath_list


def load_conf_info(load_info: dict) -> None:
    """
    加载所有json文件中的信息到一个字典load_info中
    """
    directory = './conf'
    # 1 获取指定目录下的所有文件
    filepath_list = get_filepath_list(directory)
    for filename in filepath_list:

        # 2 读取JSON文件内容
        with open(filename, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            for key, value in json_data.items():
                # 一级标题
                load_info[key] = value


def save_to_json(info: dict) -> None:
    """
    将字典中的内容保存为JSON格式的文件
    :param info:
    :return:
    """
    # 结果保存
    out_file = './out/result.json'
    with open(out_file, 'w', encoding='utf-8') as file:
        json.dump(info, file, ensure_ascii=False, indent=4)


def search(content, key, file_type) -> bool:
    extension = file_type.lower()
    if extension == "csv":

        # 遍历content中的每一个键，找到与参数key匹配度最高的那个键
        # 如果这个匹配值>阈值，则认为是同一个键，如果对应的列存在内容，则返回true
        matchResult = extractOne(key, content.keys())
        matchKey = matchResult[0]
        matchRatio = matchResult[1]

        if matchRatio >= 60:
            print("matchKey:", matchKey, "; key:", key, "; ratio:", matchRatio)
            # 获取key对应的value
            value = content.get(matchKey)
            # 遍历value中的每一个内容
            if value is not None:
                for item in value:
                    # 如果内容不为空/空白符 说明有内容 则返回true
                    if item.strip():
                        return True
            # 如果所有行都为空 则说明没有内容 返回false
            return False
        else:
            return False
    elif extension == "xml":
        return xmlMatch.match_xml(content, key)

def search2(content, key) -> bool:
    # 内容匹配，后续工作重点，调研
    pass


def draw_content(filename) -> Any:
    # 提取内容
    # 读取文件的后缀名
    extension = filename.split(".")[-1].lower()

    if extension == "csv":
        # 读取文件的内容，存储为一个map，key为列名，value为这一列的所有内容
        content = read_csv_to_map(filename)
        return content
    elif extension == "xml":
        # 获取文件对象
        return xmlContent.content_xml(filename)


def read_csv_to_map(file_path):
    """
    将csv文件转化为map
    :param file_path:
    :return:
    """
    data_map = {}
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # 读取第一行作为键
        for header in headers:
            data_map[header] = []

        for row in reader:
            for i, value in enumerate(row):
                data_map[headers[i]].append(value)

    return data_map

def process(Log_file_name: str, load_info: dict):
    # 1 提取日志内容
    content = draw_content(Log_file_name)
    # 遍历一级标题及其对应的vale
    for key, value in load_info.items():
        # 遍历二级标题及其对应的value
        for key_2, value_2 in value.items():
            # 2 设计匹配机制，将匹配后的信息写入 load_info 中
            cur_key = str(key) + '_' + str(key_2)
            extension = Log_file_name.split(".")[-1].lower()
            if search(content, cur_key, extension) is True:
                load_info[key][key_2]["status"] = 1
            else:
                load_info[key][key_2]["status"] = 0


def main():
    # 记录开始时间
    start_time = time.time()

    load_info = {}
    # Log_file_name = "./log/log.xml"
    Log_file_name = "./log/log.csv"
    # Log_file_name = "./log/log(big).csv"
    # 1 读取配置信息到 load_info 中
    load_conf_info(load_info)

    # 2 读取日志文件，匹配信息
    process(Log_file_name, load_info)

    # 3 将 load_info 写入 json
    save_to_json(load_info)

    # 记录结束时间
    end_time = time.time()

    # 计算执行时间
    execution_time = end_time - start_time

    print("程序执行时间：", execution_time, "秒")


if __name__ == '__main__':
    main()
    print("result.json结果文件已生成...")
