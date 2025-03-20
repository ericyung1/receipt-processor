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
    hour, minute = map(int, time_str.split(":"))
    return (hour == 14 and minute > 0) or (hour == 15)

def calculate_total_points(receipt):
    points = alphanumeric_length(receipt["retailer"])

    if is_round_dollar(receipt["total"]):
        points += 50

    if is_multiple_of_quarter(receipt["total"]):
        points += 25

    points += (len(receipt["items"]) // 2) * 5

    for item in receipt["items"]:
        desc = item["shortDescription"].strip()
        if len(desc) % 3 == 0:
            price = math.ceil(float(item["price"]) * 0.2)
            points += price

    if is_day_odd(receipt["purchaseDate"]):
        points += 6

    if is_between_two_and_four(receipt["purchaseTime"]):
        points += 10

    return points