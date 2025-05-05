import os

# 获取指定文件夹下的所有文件路径
def get_all_file_paths(folder_path):
    file_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

