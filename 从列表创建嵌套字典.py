"""
作为值的嵌套字典指的是一个字典作为另一个字典中键的值存储。例如：

employee = {
    "name": "John Doe",
    "contact": {
        "email": "johndoe@example.com",
    }
}
在这里，字典{"email": "johndoe@example.com",}是employee字典中"contact"键的值。

编写一个程序，将整数列表的每个元素与字典的每个项映射，形成一个嵌套字典。

定义函数map_list_dict()，它有两个参数input_dict和input_list。
在函数内部，将列表的每个元素映射到字典的相应键值对
形成一个新的字典，列表元素作为键，嵌套字典（包含输入字典的单个键值对）作为值并打印。
示例输入
{"a": 1, "b": 2, "c": 3}
6 7 8
示例输出
{6: {'a': 1}, 7: {'b': 2}, 8: {'c': 3}}
输入字典和列表中的元素数量保证相等。
仔细观察示例1，以了解如何将列表元素与字典的键值对映射。
"""

# 使用json模块解析输入并处理JSON数据
import json

def map_list_dict(input_dict, input_list):
    # 在这里编写你的代码
    return {item: {key: value} for item, (key, value) in zip(input_list, input_dict.items())}
# 获取输入字符串并将其解析为json
input_dict = json.loads(input())
# 获取整数输入并将其转换为列表
input_list = list(map(int, input().split()))
# 调用函数
print(map_list_dict(input_dict, input_list))