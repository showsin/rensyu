"""
编写一个程序，检查是否可以通过连接给定的较小列表来形成目标列表。

定义函数 can_form_target()，该函数有两个参数：list_of_lists（整数列表的列表）和 target_list（整数列表）。
在函数内部，将 list_of_lists 中的所有列表连接起来，并与 target_list 进行比较。如果它们相同（忽略顺序），则返回 True，否则返回 False。

输入格式为
number_of_smaller_lists(n)  => 小列表的数量
smaller_list_1  => 小列表1
smaller_list_2  => 小列表2
...
smaller_list_n  => 小列表n
target_list     => 目标列表

示例输入
2
1 2 3
4 5
1 2 3 4 5

示例输出
True

解释:
可以通过连接 [1, 2, 3] 和 [4, 5] 形成 [1, 2, 3, 4, 5]。

你可以使用 list.sort() 方法对列表进行排序。
忽略列表中元素的顺序，只要元素相同(出现次数也需要相同)，就认为两个列表相同。
"""

def can_form_target(list_of_lists, target_list):
    # 在这里编写你的代码
    flat_list = [item for sublist in list_of_lists for item in sublist]
    return sorted(flat_list) == sorted(target_list)
# 获取用户输入
user_list_of_lists = [list(map(int, input().split())) for _ in range(int(input()))]
user_target_list = list(map(int, input().split()))

# 调用函数
print(can_form_target(user_list_of_lists, user_target_list))

