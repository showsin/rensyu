"""
编写一个程序将嵌套列表扁平化为一维列表(即元素均不是列表)。

定义函数flatten_list()，该函数有一个参数list_of_lists。
在函数中，创建一个新的一维列表，其中包含子列表中的所有元素。
返回新创建的列表。
输入格式为：

n         => 列表的数量
list_1    => 列表1
list_2    => 列表2
...
list_n    => 列表n
示例输入
2
0 1 2 3
4 5
示例输出
[0, 1, 2, 3, 4, 5]
你可以使用for循环嵌套来遍历嵌套列表。
保证输入的列表中的元素都是整数。
"""

def flatten_list(list_of_lists):
    # 在此处编写你的代码
    # my_list = [item for sublist in list_of_lists for item in sublist]
    # return my_list
    result = []
    for item in list_of_lists:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# 初始化嵌套列表
list_of_lists = []

# 获取用户输入
# 子列表的数量
n = int(input())

# 子列表
for _ in range(n):
    sublist = list(map(int, input().split()))
    list_of_lists.append(sublist)

# 调用函数
print(flatten_list(list_of_lists))