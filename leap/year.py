# Solution to the Leap exercise
# Given a year, determine whether it is a leap year
# Leap years are divisible by 4
# except when divisible by 100
# unless when divisible by 400


def is_leap_year(year=0):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
