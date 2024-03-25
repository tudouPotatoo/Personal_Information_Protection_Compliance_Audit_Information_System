import LoadConfInfo
import os
def extract(text, begin, end, begin_point=0):
    p = text.find(begin, begin_point)
    if p == -1:
        # 没有找到begin的话
        return None

    e = text.find(end, p)
    if e == -1:
        # 没有找到end的话
        return None
    return text[p + len(begin): e], e + len(end)


def match_xml(content, key):
    """
    在xml日志中查找是否包含key对应的内容
    :param content:
    :param key:
    :return:
    """
    last_endpoint = 0
    if content is not None:
        info = extract(content, "<folder>", "</folder>", last_endpoint)
        text, last_endpoint = info
        key_1 = key.split("_")[0]
        key_2 = key.split("_")[-1]
        try:
            key_1 = extract(text, "<" + str(key_1) + ">", "</" + str(key_1) + ">", 0)[0]
            key_2 = extract(key_1, "<" + str(key_2) + ">", "</" + str(key_2) + ">", 0)[0]
            if key_2.strip():
                return True
            else:
                return False
        except Exception as e:
            return False
