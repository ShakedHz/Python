"""
exercise 1
Shaked Horovitz
"""


def str_to_digit(digit_str: str):
    """
    This function gets name of digit (digit_str) and returns the digit as an integer.
    If the value of digit_str is not a name of a digit, it returns False.
    :param digit_str: string
    :return: int/bool
    """
    digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
              "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    if digit_str not in digits:
        return False
    return digits[digit_str]


