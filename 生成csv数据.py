import os
import csv
import random


def write_text_to_csv_files(folder_path):
    # 遍历文件夹中的所有文件
    # 生成50个随机数字
    numbers = [random.randint(0, 100) for _ in range(50)]
    
    rows = [numbers[i:i+10] for i in range(0, len(numbers), 10)]


    for file_name in os.listdir(folder_path):
        # 如果文件不是CSV文件，则跳过
        if not file_name.endswith(".csv"):
            continue

        # 构建CSV文件的完整路径
        file_path = os.path.join(folder_path, file_name)

        # 打开文件以追加模式写入文本
        with open(file_path, "a", newline="") as csv_file:

            
            # 创建一个写入器对象
            writer = csv.writer(csv_file)
            # 写入其他文本和字符
            for row in rows:
                writer.writerow(row)
            csv_file.write("这是一些其他文本和字符\n")
            csv_file.write("Hello, world!\n")

# 遍历paperFile文件夹并向所有CSV文件写入文本和字符
write_text_to_csv_files("./paperFile")
