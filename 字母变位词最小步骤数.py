"""
编写一个程序，计算从两个字符串中移除的最少字母数，使它们成为变位词。

变位词是指可以通过重新排列字符而形成的字符串。例如，dab 是 bad 的变位词。

定义函数 min_removals_to_anagram()，有两个参数：str1 和 str2。
在函数内，计算从两个字符串中移除的最小字母数，使它们成为变位词。

示例输入
cab
base
示例输出
3

解释:
需要移除cab 中的c，base 中的s 和 e。最小移除数3，成为变位词ab 和 ba
"""
from collections import Counter


def min_removals_to_anagram(str1, str2):
    # 此处编写代码
    count1 = Counter(str1)
    count2 = Counter(str2)
    common = 0
    konw_count = count1 & count2
    for char in konw_count:
        common += min(count1[char], count2[char])
    return len(str1) + len(str2) - 2 * common

# 获取输入
str1 = input()
str2 = input()

# 调用函数，输出结果
print(min_removals_to_anagram(str1, str2))