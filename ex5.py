"""
exercise 5
Shaked Horovitz
"""

import json


def save_data(file_path, objects_list):
    """
    This function gets a file path and an objects list.
    The function writes the list to the file by converting it to json format.
    :param file_path: string
    :param objects_list: list
    :return: None
    """
    with open(file_path, "w") as fp:
        json.dump(objects_list, fp)


def load_data(file_path):
    """
    This function gets a file path and returns the list
    with the original objects types from the file.
    :param file_path: string
    :return: list
    """
    with open(file_path, 'rb') as fp:
        objects_list = json.load(fp)
        return objects_list
