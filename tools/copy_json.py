import json

def extract_data(input_file, output_file, start, end):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for idx, line in enumerate(f_in):
                if start <= idx < end:
                    f_out.write(line)
                elif idx >= end:
                    break

# 用法示例
input_file = '/home/gofuuu/BEVFormer/data/nuscenes/v1.0-trainval/backup_sample.json'  # 输入的 JSON 文件名
output_file = '/home/gofuuu/BEVFormer/data/nuscenes/v1.0-trainval/sample.json'  # 输出的 JSON 文件名
start_line = 0  # 起始行
end_line = 70841  # 结束行

extract_data(input_file, output_file, start_line, end_line)


