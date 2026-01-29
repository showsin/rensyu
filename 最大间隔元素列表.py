"""
编写程序确定一个已排序整数列表的最大间隔。

间隔是指有序整数列表中两个连续元素之间的差值。

例如，在列表[1, 6, 9, 16]中，1和6之间的间隔是5，6和9之间的间隔是3，9和16之间的间隔是7。

因此，给定列表中的最大间隔是7。

定义函数max_gap()，参数为整数列表lst。
在函数内，对列表进行排序，然后找出两个连续元素之间的最大差值。
返回最大差值。
"""

def max_gap(lst):
    # 此处编写代码
    sorted_list = sorted(lst)
    max_diff = 0
    return max((sorted_list[i] - sorted_list[i - 1]) for i in range(1, len(sorted_list)))

# 获取用户输入，转换为整数列表
numbers = list(map(int, input().split()))
# 调用函数，输出结果
print(max_gap(numbers))