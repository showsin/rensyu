"""
编写一个程序，确定给定字符串中子字符串的重复次数。

定义函数repetitions_in_string()，该函数接受一个字符串参数。
在函数中，返回提供的字符串中子字符串的重复次数。
注意：如果字符串不是由单个子字符串重复形成的，则输出应为1。

例如，在字符串pythonpropro中，子串pro重复了两次，但是这种重复本身不能形成完整的字符串。因此输出为1。

示例输入
dededededede
示例输出
6
解释:
de重复6次形成dededededede

假设字符串长度为n，则子字符串的长度可以从1到n-1，从长度小的子串开始尝试，满足条件即返回。
"""


def repetitions_in_string(s):
    # 此处编写代码
    for lenth in range(1, len(s)):

        if len(s) % lenth == 0:
            count = len(s) // lenth
            if s[:lenth] * count == s:
                return count
    return 1


# 获取输入
test_string = input()

# 调用函数
print(repetitions_in_string(test_string))
