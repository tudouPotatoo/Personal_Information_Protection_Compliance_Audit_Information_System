# 读取日志文件并提取每一行日志的最后部分
def process_log_file(input_file, output_file):
    with open(input_file, 'r', encoding='gb18030') as f:
        lines = f.readlines()

    # 使用split(']')方法以右方括号作为分隔符，将当前行line分割成多个部分，并取分割后的最后一个部分。
    # 去掉开头的-连字符和空白符
    processed_lines = [line.split(']')[-1].lstrip().lstrip('-').lstrip() for line in lines]

    # 将提取的内容保存到输出文件中
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(processed_lines))


def main():
    # 输入和输出文件的路径
    input_file = 'log/syslog-why.log'
    output_file = 'log/cleaned_big.log'

    # 处理日志文件
    process_log_file(input_file, output_file)

if __name__ == '__main__':
    main()
    print("cleaned.log结果文件已生成...")
