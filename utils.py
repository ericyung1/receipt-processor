import re
import math
from datetime import datetime

def alphanumeric_length(s):
    return len(re.sub(r'[^a-zA-Z0-9]', '', s))

def is_round_dollar(price):
    return float(price).is_integer()

def is_multiple_of_quarter(price):
    return float(price) % 0.25 == 0

def is_day_odd(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    day = date_obj.day
    return day % 2 == 1

def is_between_two_and_four(time_str):
    hour = int(time_str.split(":")[0])
    return 14 < hour < 16