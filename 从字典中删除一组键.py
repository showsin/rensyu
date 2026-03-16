"""
编写一个程序，使用提供的键列表从字典中删除指定的键集合。

定义函数remove_keys()，有两个参数：字典dict_input和键列表key_list。
在函数中，从字典中删除key_list中存在的所有键。
返回更新后的字典。
示例输入
{"fruit": "Apple", "color": "Red", "price": 10}
color price
示例输出
{'fruit': 'Apple'}
解释:
在这里，列表color和price是字典中存在的指定键，需要被删除。因此，最终更新后的字典不包含color和price。

使用del语句删除字典中的键，如果键不存在，则会引发KeyError异常。需要考虑下异常。
使用pop方法删除字典中的键，如果键不存在，则不会引发异常，建议用此方法。
"""

def remove_keys(dict_input, key_list):
    # 此处编写代码
    for key in key_list:
        if key in dict_input:
            del dict_input[key]
    return dict_input

# 获取输入
user_dict = eval(input())
user_key_list = input().split()

# 调用函数
print(remove_keys(user_dict, user_key_list))