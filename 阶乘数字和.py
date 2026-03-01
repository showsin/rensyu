"""
编写一个程序来计算一个数字的阶乘，并计算该阶乘的各位数字之和。

定义函数sum_of_digits_in_factorial()的函数，参数为num。
在函数内，首先计算num的阶乘，然后返回阶乘中数字的和。
数字num的阶乘是从1到num的所有数字的乘积。例如，阶乘5是1 * 2 * 3 * 4 * 5 = 120，则其阶乘的数字和为1 + 2 + 0 = 3。

示例输入
24
示例输出
81
数字0的阶乘为1。
"""
import math


def sum_of_digits_in_factorial(num):
    # 在此处编写你的代码\
    s = 0
    for n in str(math.factorial(num)):
        s += int(n)
    return s


# 获取用户输入
num = int(input())

# 调用函数
print(sum_of_digits_in_factorial(num))
