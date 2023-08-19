import os
import shutil

def copy_favorites():
    """复制导航的静态文件到博客的目录"""
    links_path = os.path.join(r"D:\code\next\link\out")
    favorites_path = os.path.join(r"D:\code\next\favorites")
    # 如果目录不存在则创建
    if not os.path.isdir(favorites_path):
        os.makedirs(favorites_path)
    if os.path.isdir(links_path):
        shutil.copytree(links_path, favorites_path, dirs_exist_ok=True)
        print("导航的静态文件到博客的目录中！")
    