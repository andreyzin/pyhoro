from datetime import date
from ..enums import ZodiacTitle
from .zodiacs import zodiacs
from bisect import bisect


def get_zodiac_of_date(date: date) -> ZodiacTitle:
    return zodiacs[bisect(zodiacs, (date.month, date.day))][2]
