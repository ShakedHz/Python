"""
exercise 2
Shaked Horovitz
"""
from functools import reduce

def sum_of_list(list):
     """
     The function above gets list and return its sum.
     :param list: list
     :return: int
     """
     return reduce(lambda x, y: x + y, list)

