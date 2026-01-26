"""
编写一个程序，将每个单词的最后一个字母大写。

定义函数capitalize_last_letter()，参数为sentence(字符串)。
该函数应返回每个单词最后一个字母大写的字符串。
"""


def capitalize_last_letter(sentence):
    # 在此处编写你的代码
    list_sent = sentence.split()
    list_sent = [i[:-1] + i[-1].upper() if i.isalpha() else i for i in list_sent]
    return ' '.join(list_sent)
# 获取用户输入
sentence = input()

# 调用函数
print(capitalize_last_letter(sentence))
