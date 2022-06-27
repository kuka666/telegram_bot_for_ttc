import pandas
import json
from datetime import date


def between_date_day(from_date, to_date):
    from_date = from_date.split(".")
    to_date = to_date.split(".")
    result_date = date(int(to_date[2]), int(to_date[1]), int(
        to_date[0])) - date(int(from_date[2]), int(from_date[1]), int(from_date[0]))
    return result_date.days


