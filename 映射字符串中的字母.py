"""
编写一个程序，创建一个字典，其中给定单词的每个唯一字母表示一个键，值为字母出现的索引的列表。

定义函数letter_indices()，参数为word(字符串)。
在函数中，创建一个字典，其中键是单词中的唯一字母，值是包含该字母出现的索引的列表。
返回该字典

示例输入
pineapple
示例输出
{'p': [0, 5, 6], 'i': [1], 'n': [2], 'e': [3, 8], 'a': [4], 'l': [7]}

解释:
给定字符串中的唯一字母是p，i，e，a和l，它们是字典的键。 而键的值是它们出现的索引(注意索引从0开始)
"""


def letter_indices(word):
    # 此处编写代码
    # new_dict = {}
    new_dict = {letter: [] for letter in word}
    for i, letter in enumerate(word):
        new_dict[letter].append(i)
    return new_dict


# 获取输入
word = input()

# 调用函数
print(letter_indices(word))
