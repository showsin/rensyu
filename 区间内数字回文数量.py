"""
编写一个Python程序，计算给定范围内的回文数的数量。
回文数是指当其数字反转时仍然保持相同的数字。
例如，数字像121，1，22是回文数，因为它们的数字在反转时仍然保持相同。

定义函数count_palindromes()的函数，有两个参数：start_number和end_number。
在函数中，返回回文数的总计数，即在start_number和end_number之间的回文数量。

示例输入
10
20

示例输出
1

start_number和end_number都是包含的。
数字转为字符串，然后使用切片[::-1]反转字符串，判断是否为回文数。
"""


def count_palindromes(start_number, end_number):
    # 此处编写代码
    count = 0
    for number in range(start_number, end_number+1):
        if str(number) == str(number)[::-1]:
            count += 1
    return count
# 获取输入
start_number = int(input())
end_number = int(input())
# 调用函数
print(count_palindromes(start_number, end_number))