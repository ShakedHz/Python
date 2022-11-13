"""
exercise 4
Shaked Horovitz
"""

def count_num_of_0_and_8(low_num,high_num):
    """
    This function gets two numbers - low_num and high_num, that represent a range.
    The function counts how many numbers in the range contain the digits 0 or 8 and returns it.
    :param low_num: int
    :param high_num: int
    :return: int
    """
    return count if ([count:=0],[count:=count+1 for num in range(low_num,high_num+1) if '0' in str(num) or '8' in str(num)]) else None
