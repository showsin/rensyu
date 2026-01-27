"""
编写一个程序来查找两个列表中的相同元素。

定义函数find_common_elements()，它接受两个整数列表参数，list1和list2。
在函数内部，找到共同的数字，并按升序返回它们。
"""


def find_common_elements(list1, list2):
    # 此处编写代码

    return sorted(set(list1) & set(list2))


# 获取用户输入，转换为列表
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 调用函数
print(find_common_elements(list1, list2))