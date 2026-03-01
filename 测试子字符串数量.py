"""
编写一个程序来检查给定的字符串是否为另一个字符串的子集。

定义函数is_subset()，有两个参数：sub_string和main_string(均是字符串)。
在函数内，如果sub_string是main_string的子集，则返回True，否则返回False。
例如，abc是abracadabra的子集，因为abc中的每个字符都在abracadabra中出现。

示例输入
march
charming
示例输出
True
忽略字符串中字符出现的顺序，也忽略字符出现的次数。

"""

def is_subset(sub_string, main_string):
    # 在此处编写你的代码
    # for char in sub_string:
    #     if char not in main_string:
    #         return False
    # return True
    return set(sub_string).issubset(set(main_string))
# 获取用户输入
sub_string = input()
main_string = input()

# 调用函数
print(is_subset(sub_string, main_string))