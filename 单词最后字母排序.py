"""
编写一个程序，按照每个单词的最后一个字母对句子进行排序。

定义函数sort_by_last_char()，参数为sentence(表示句子)。
在函数内部，返回按照每个单词最后一个字母排序的句子。

示例输入
i love python programming

示例输出
love programming i python
"""



def sort_by_last_char(sentence):
    # 此处编写代码
    words = sentence.split()
    words.sort(key=lambda x: x[-1])
    return ' '.join(words)
# 输入句子
sentence = input()

# 调用函数
print(sort_by_last_char(sentence))