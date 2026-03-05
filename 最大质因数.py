"""
编写一个程序来确定给定数字的最大质因数。

例如，42的质因数是2，3和7。
因此，7是42的最大质因数。

定义函数largest_prime_factor()，它接受一个参数num。
在函数内部，计算并返回num的最大质因数。
示例输入
1267
示例输出
181
解释:
1267的质因数是7和181。其中181是最大的。

注意质因数首先是质数，所以必须满足质数的条件。
"""


import sympy


def largest_prime_factor(num):
    # 此处编写代码
    if num < 2:
        return None

    max_factor = -1

    while num % 2 == 0:
        max_factor = 2
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            max_factor = i
            num //= i
        i += 2

    if num > max_factor:
        max_factor = num
    return max_factor


    # if num < 2:
    #     return None
    #     # factorint() 函数返回质因数分解的字典：键是质因数，值是对应的指数
    # prime_factors = sympy.factorint(num)
    # # 取字典的键（所有质因数）中的最大值
    # return max(prime_factors.keys())


# 获取输入数字
user_input = int(input())

# 调用函数
print(largest_prime_factor(user_input))
