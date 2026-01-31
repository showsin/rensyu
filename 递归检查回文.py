"""
编写一个程序递归判断一个字符串是否为回文。

回文是指从前往后读和从后往前读都一样的单词、短语、数字或其他字符序列。在本挑战中，空字符串也被视为回文。

递归是一种编程概念，涉及在函数的定义中调用自身。

定义函数is_string_palindrome()，参数为string。
在函数内部，实现递归，如果字符串是回文，则返回True，否则返回False。
"""


def is_string_palindrome(string):
    # 此处编写代码
    if len(string) <= 2 and string[0] == string[-1]:
        return True
    elif string[0] == string[-1]:
        return is_string_palindrome(string[1:-1])
    else:
        return False

# 获取用户输入
user_input = input()

# 调用函数
print(is_string_palindrome(user_input.lower()))