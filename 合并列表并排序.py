"""
编写一个程序，将两个列表合并，并按照第一个列表的顺序对合并后的列表进行排序。

定义一个名为merge_and_sort()的函数，其中有两个列表参数，first_list和second_list。
在函数内部，合并两个列表。
检查第一个列表是升序还是降序排列。
按照第一个列表的顺序对合并后的列表进行排序。
返回排序后的列表。
"""


def merge_and_sort(first_list, second_list):
    # 此处编写代码
    new_list = first_list + second_list
    s1 = sorted(first_list)

    return sorted(new_list) if first_list == s1 else sorted(new_list, reverse=True)



# 获取输入，转换为列表
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

# 调用函数
print(merge_and_sort(first_list, second_list))
