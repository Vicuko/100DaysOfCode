def is_leap(year):
    divisible_by_4 = (year % 4 == 0)
    divisible_by_100 = (year % 100 == 0)
    divisible_by_400 = (year % 400 == 0)

    leap_year = False
    if (divisible_by_4 and not divisible_by_100) or (divisible_by_400):
        leap_year = True

    return leap_year


def days_in_month(year, month):
    """"Take a year and a month number
    and return the number of days in such
    month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] += 1
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
