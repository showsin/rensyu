"""
编写一个程序，根据某个条件过滤字典值。
对于这个挑战，条件是字典值应该大于整数k。

定义函数filter_dict_values()，有两个参数：字典mixed_dict和整数k。
在函数内部，创建一个新字典，并从mixed_dict过滤值不是整数或大于整数k的键值对，然后存储到新字典中。
返回新字典。
示例输入
{'cat': 2, 'dog': 5, 'parrot': 'yellow', 'fish': 1}
3
示例输出
{'dog': 5, 'parrot': 'yellow'}
解释:
在输出中，过滤后的字典包含一个大于3（k的输入值）的整数值，以及一个不是整数的值yellow。

使用for循环遍历字典中的每一项，然后使用if语句检查值是否是整数或大于整数k。
判断值是否是整数，可以使用type()函数，然后检查返回值是否等于int。
"""

def filter_dict_values(mixed_dict, k):
    # 此处写下你的代码
    new_dict = {}
# 获取输入
user_dict = eval(input())
user_k = int(input())

# 调用函数
print(filter_dict_values(user_dict, user_k))