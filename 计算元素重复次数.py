"""
编写一个程序，计算列表中每个元素的出现的次数，并以字典返回。

定义函数count_frequency()，该函数接受一个元素列表lst作为参数。
在函数内部，返回一个字典，其中列表的元素作为键，其相应的次数作为值。

示例输入
run jump run swim swim run run

示例输出
{'run': 4, 'jump': 1, 'swim': 2}
"""

def count_frequency(lst):
    # 此处编写代码
    new_dict = {}
    for word in lst:
        new_dict[word] = new_dict.get(word, 0) + 1
    return new_dict
# 获取用户输入
lst = list(input().split())

# 调用函数
print(count_frequency(lst))