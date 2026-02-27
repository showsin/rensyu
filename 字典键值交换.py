"""
编写一个程序来交换字典的键和值。

定义函数swap_dict()，参数为一个字典dict。
在函数内部，反转给定字典的键和值。如果一个值出现多次，将对应键组合在一个列表中。

示例输入
{'Pizza': 'Food', 'Pasta': 'Food', 'Water': 'Drink', 'Coke': 'Drink'}
示例输出
{'Food': ['Pizza', 'Pasta'], 'Drink': ['Water', 'Coke']}

解释:
输入中Food的值出现多次，因此Food的键被保留在一个列表中['Pizza','Pasta']。
"""

def swap_dict(dict):
    # 此处编写代码
    new_dict = {value: [] for value in dict.values()}
    for key, value in dict.items():
        new_dict[value].append(key)
    return new_dict
# 读取输入的字典
dict = eval(input())

# 调用函数
print(swap_dict(dict))
