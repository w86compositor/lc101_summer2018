# The first solution is using the library calendar modulo which has the leap year implemented.
# import calendar
# print(calendar.isleap(1900)

# This is the mathematical solution


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap(1956))
