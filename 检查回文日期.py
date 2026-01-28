"""
编写一个程序，检查给定日期是否为dd/mm/yyyy和mm/dd/yyyy格式的回文日期。

定义函数is_date_palindromic()，接受一个参数date_in_string（以dd/mm/yyyy格式的日期字符串）。
如果给定的日期在dd/mm/yyyy和mm/dd/yyyy格式下都是回文日期，函数应该返回True，否则返回False。
"""


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_valid_date(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month[month - 1]:
        return False
    return True


def is_date_palindromic(date_in_string):
    # 此处编写你的代码
    parts = date_in_string.split('/')
    if len(parts) != 3:
        return False
    day_str, month_str, year_str = parts
    if len(day_str) != 2 or len(month_str) != 2 or len(year_str) != 4:
        return False

    try:
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)

    except ValueError:
        return False

    if not is_valid_date(day, month, year):
        return False

    date_str1 = day_str + month_str + year_str
    date_str2 = month_str + day_str + year_str

    return (date_str1 == date_str1[::-1]) and (date_str2 == date_str2[::-1])


# 获取日期输入
date_in_string = input()

# 调用函数
print(is_date_palindromic(date_in_string))
