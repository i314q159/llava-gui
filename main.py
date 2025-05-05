import os
import requests

def get_all_file_paths(folder_path):
    file_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def get_response(url, picture_path):
    data = {
        "model": "llava",
        "prompt": "图片里面是什么?",
        "images": [picture_path],
    }

    response = requests.post(url, json=data)
    print("图片路径: ", picture_path)
    print("状态码: ", response.status_code)


url = "http://localhost:11434/api/generate"
folder_path = "d:/wallpaper_d/"
file_paths = get_all_file_paths(folder_path)

for file_path in file_paths:
    get_response(url, file_path)
