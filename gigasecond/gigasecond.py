from datetime import datetime, timedelta

def add_gigasecond(birthday):
    return birthday + timedelta(seconds=10**9)
