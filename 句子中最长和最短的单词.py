"""
编写一个程序来找出句子中最长和最短的单词。不要忽略字母数字或空格字符。

定义函数extreme_words_in_sentence()的函数，参数为一个。
在函数内部，返回一个元组，元组中有两个元素：句子中最长的单词和最短的单词。
如果多个单词具有相同的长度，则返回第一个出现的。
另外返回的最长单词和最短单词应该是小写的。

示例输入-1
We took 2 hours break in a week
示例输出-1
('hours', '2')
解释:
在测试输入中，最长的单词是hours和break。由于hours先出现，因此它出现在输出中。类似地，2和a是最短的单词。但是由于2在句子中先出现，因此它被包含在输出中。

示例输入-2
Python is both challenging and fun.
示例输出-2
('challenging', 'is')
使用max()和min()函数来找到最长和最短的单词。
使用str.split()函数将句子分割成单词。
使用str.lower()函数将句子中的所有字母转换为小写。
"""

# def extreme_words_in_sentence(sentence):
#     # 此处编写你的代码
#     sentence = sentence.lower()
#     words = sentence.split()
#     longest_word = max(words, key=len)
#     shortest_word = min(words, key=len)
#     return (longest_word, shortest_word)


import numpy as np
def extreme_words_in_sentence(sentence):
    """
    使用numpy进行向量化操作
    """
    sentence = sentence.lower()
    lower_words = sentence.split()

    lengths = np.array([len(word) for word in lower_words])

    min_idx = np.where(lengths == lengths.min())[0][0]
    max_idx = np.where(lengths == lengths.max())[0][0]

    return (lower_words[max_idx], lower_words[min_idx])

# 处获取输入
sentence = input()
# 调用函数
print(extreme_words_in_sentence(sentence))