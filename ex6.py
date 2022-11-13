"""
exercise 6
Shaked Horovitz
"""

from datetime import date, datetime
DAYS_IN_YEAR = 365

def days_to_birthday(birthday):
    """
    This function gets a birthday and returns the days until it.
    :param birthday: datetime.date
    :return: int
    """
    today = date.today()
    today = datetime.strptime(str(today), "%Y-%m-%d")
    birthday = date(today.year, birthday.month, birthday.day)
    birthday = datetime.strptime(str(birthday), "%Y-%m-%d")
    if today > birthday:
        days = DAYS_IN_YEAR - (today - birthday).days
    elif today < birthday:
        days = (birthday - today).days
    else:
        days = "Your birthday is today. Happy birthday!"
    return days

