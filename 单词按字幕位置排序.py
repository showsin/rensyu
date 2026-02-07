"""
编写一个程序，根据给定位置的字符对单词进行排序。
定义函数sort_words_by_char()，它接受两个参数，一个words列表和一个index(位置)。
在函数内，根据每个单词中给定位置的字符对列表进行排序。按字母升序排列。
该函数应返回排序后的列表。

示例输入
helium oxygen nitrogen
4

示例输出
['oxygen', 'helium', 'nitrogen']
解释:
helium的第4个位置字母是i，oxygen是g，nitrogen是r。这些字母的升序是g，i和r。

输入的位置从1开始，但字符串索引从0开始
"""


def sort_words_by_char(words, index):
    # 在此处编写代码
    return sorted(words, key=lambda x: x[index-1])
# 获取用户输入
words = input().split() # 单词列表
index = int(input())    # 位置

# 调用函数
print(sort_words_by_char(words, index))