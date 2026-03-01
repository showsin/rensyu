"""
编写一个程序来确定给定字符串是否为异位词。

异位词是指没有字母重复出现的单词、短语或句子。

定义函数is_heterogram()，参数为字符串s。
在函数内，如果字符串是异位词，则返回Yes，否则返回No。

示例输入
the big dwarf only jumps
示例输出
Yes

该函数区分大小写，即字母s 和 S是不同的。
"""

def is_heterogram(s):
    # 此处编写代码
    if len(''.join(s.split())) != len(set(''.join(s.split()))):
        return "No"
    return "Yes"
# 获取输入
input_string = input()

# 调用函数，输出结果
print(is_heterogram(input_string))