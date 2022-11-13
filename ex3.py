"""
exercise 3
Shaked Horovitz
"""

LETTERS_TO_REMOVE = ['a', 'u', 'e', 'o', 'i']


def remove_letters_from_str(string: str) -> str:
    """
    This function gets a string and returns the string without the letters a,u,e,o,i
    :param string: string
    :return: string
    """
    return "".join(c for c in string if c not in LETTERS_TO_REMOVE)

