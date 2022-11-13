"""
exercise 7
Shaked Horovitz
"""

import shutil
import os


def copy_files(src_dir, dest_dir, extensions_list):
    """
    This function gets source directory, destination directory and extensions list.
    The function copies from src_dir only the files that their extension is in extensions list
    (works with subdirectories too).
    :param src_dir: string
    :param dest_dir: string
    :param extensions_list: list
    :return: None
    """
    objects = os.listdir(src_dir)
    for obj in objects:
        path = os.path.join(src_dir, obj)
        if os.path.isfile(path):
            if not extensions_list:
                shutil.copy(path, dest_dir)
            else:
                split_extension = obj.split(".")
                if split_extension[1] in extensions_list:
                    shutil.copy(path, dest_dir)
        else:
            dir_path = os.path.join(dest_dir, obj)
            os.mkdir(dir_path)
            copy_files(os.path.join(src_dir, obj), os.path.join(dest_dir, obj), extensions_list)


copy_files("/Users/shake/Documents/src", "/Users/shake/Documents/dest", ["docx","rar"])





