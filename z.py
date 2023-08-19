import os
import shutil
import subprocess
import time

def copy_favorites():
    """复制导航的静态文件到博客的目录"""
    links_path = os.path.join(r"D:\code\next\link\out")
    favorites_path = os.path.join(r"D:\code\next\favorites")
    # 如果目录不存在则创建
    if not os.path.isdir(favorites_path):
        os.makedirs(favorites_path)
    if os.path.isdir(links_path):
        shutil.copytree(links_path, favorites_path, dirs_exist_ok=True)
        print("已经复制导航的静态文件到项目的目录中！")
    
    while True:
        # 1. 添加所有更新进入git的本地仓库
        subprocess.run(["git", "add", "."])

        # 添加更新信息
        subprocess.run(["git", "commit", "-m", "更新"])

        # 2. 同步到远程仓库
        while True:
            result = subprocess.run(["git", "push", "origin", "main"])
            if result.returncode == 0:
                # 如果成功同步到远程仓库，退出内部循环
                break
            else:
                # 如果同步失败，等待一段时间后继续重试
                time.sleep(100)

        # 检查上一步操作的返回值
        if subprocess.run(["git", "rev-parse", "--quiet", "--verify", "HEAD"]).returncode == 0:
            # 如果成功同步到远程仓库，退出外部循环
            break
        else:
            # 如果同步失败，等待一段时间后继续重试
            time.sleep(100)


if __name__ == "__main__":
    copy_favorites()