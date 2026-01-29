"""
编写一个程序找出两个单词之间的共同字母。

定义函数common_letters()，它接受两个参数:word1和word2。
该函数应返回一个包含word1和word2之间均出现的字母的组成的字符串。
返回的字符串中的字母应为小写并按字母顺序排序。
如果没有相同的字母，则返回一个空字符串。
"""


def common_letters(word1, word2):
    # 此处编写代码
    new_list = sorted(set(word1) & set(word2))
    new_str = ''.join(new_list).lower()

    return new_str

# 输入两个单词
word1 = input()
word2 = input()

# 调用函数, 并打印结果
print(common_letters(word1, word2))