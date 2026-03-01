"""
@Time   : 2026/3/1 星期日 11:40
@Author : mailiangshi@gmail.com
@File   : file_process_tools.py
该模块提供文件和目录操作的实用工具函数，主要用于：
1. 生成唯一文件名以避免文件冲突
2. 批量移动嵌套目录中的文件到根目录
3. 清理空的子目录结构
"""
import os
import shutil


def get_unique_filename(dst_dir, filename):
    """
    生成唯一的文件名，避免目标目录中已有同名文件
    :param dst_dir: 目标目录路径
    :param filename: 原始文件名
    :return: 唯一的文件名（如：file.txt -> file(1).txt）
    """
    base_name, ext = os.path.splitext(filename)
    new_filename = filename
    counter = 1

    # 检查文件是否存在，存在则添加数字后缀
    while os.path.exists(os.path.join(dst_dir, new_filename)):
        new_filename = f"{base_name}({counter}){ext}"
        counter += 1

    return new_filename


def move_all_files_to_root(root_dir):
    """
    将多层子文件夹中的文件移动到根文件夹，并删除空文件夹
    :param root_dir: 根文件夹路径
    """
    # 验证根目录是否存在
    if not os.path.isdir(root_dir):
        print(f"错误：根目录 {root_dir} 不存在！")
        return

    # 自底向上遍历目录（topdown=False），方便后续删除空文件夹
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # 跳过根目录本身，只处理子文件夹中的文件
        if root == root_dir:
            continue

        # 移动当前目录下的所有文件到根目录
        for file in files:
            # 构造文件的源路径
            src_file_path = os.path.join(root, file)
            # 生成唯一的目标文件名
            unique_filename = get_unique_filename(root_dir, file)
            # 构造文件的目标路径
            dst_file_path = os.path.join(root_dir, unique_filename)

            try:
                # 移动文件
                shutil.move(src_file_path, dst_file_path)
                print(f"已移动：{src_file_path} -> {dst_file_path}")
            except Exception as e:
                print(f"移动文件失败 {src_file_path}：{str(e)}")

        # 删除当前空文件夹
        try:
            os.rmdir(root)
            print(f"已删除空文件夹：{root}")
        except OSError as e:
            # 文件夹非空时会抛出异常，此处忽略即可
            print(f"文件夹未删除（非空）：{root} - {str(e)}")


if __name__ == "__main__":
    # ########## 请修改为你的目标根文件夹路径 ##########
    ROOT_FOLDER = r"D:\github\docs"
    # ################################################

    move_all_files_to_root(ROOT_FOLDER)
    print("\n文件迁移和空文件夹删除完成！")
