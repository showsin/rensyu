"""
编写一个程序将一个集合转换为字典。

定义函数convert_set_to_dict()，接收一个参数input_set（一个整数集合）。
在函数内部，将集合转换为字典，将集合中的每个项作为键，并将值均设为0。
按键排序字典（升序）并返回排序后的字典。
示例输入
1 2 3 4
示例输出
{1: 0, 2: 0, 3: 0, 4: 0}
需要按键排序字典(即添加键值对时需要按序添加)
"""

def convert_set_to_dict(input_set):
    # 此处写下你的代码
    new_dict = {key:0 for key in sorted(input_set)}
    return new_dict
# 获取输入，转为集合
input_set = set(map(int, input().split()))

# 调用函数
print(convert_set_to_dict(input_set))