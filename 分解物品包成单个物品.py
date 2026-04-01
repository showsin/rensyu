"""
假设你有一个物品列表，里面有各种类型的铅笔。列表中的每个物品都是一个字典，有两个键 - type 和 quantity。

type键对应一个字符串，表示铅笔的类型，而 quantity 键保存一个整数，表示该类型铅笔的数量。

编写一个程序，将一个物品列表分解成一个列表中的单个物品。

定义函数break_down_list()，参数为items。
在函数内，对列表中的每个物品，创建一个具有相同type但quantity为1的新字典。
返回新的字典列表。
示例输入
[{'type': 'HB', 'quantity': 2}, {'type': '2B', 'quantity': 3}]
示例输出
[{'type': 'HB', 'quantity': 1}, {'type': 'HB', 'quantity': 1}, {'type': '2B', 'quantity': 1}, {'type': '2B', 'quantity': 1}, {'type': '2B', 'quantity': 1}]
使用for循环遍历列表中的每个物品。
如果quantity的输入值为0，则返回空列表[]。
需要按物品出现的顺序返回新的列表。
"""
def break_down_list(items):
    # 此处编写代码
        return [{'type':item['type'],'quantity':1} for item in items for _ in range(item['quantity'])]
# 获取物品列表
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))