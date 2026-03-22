"""
编写一个程序来找出给定数字的排列。
三位数的排列是指三个不同数字的所有可能的排列。例如，数字5，6和7的排列：
567
576
657
675
756
765
定义函数get_all_permutations()，该函数接受一个包含三个整数的列表作为参数。
在函数内部，找出所有可能的数字排列，并在新行中打印每个排列。
示例输入
1 2 3
示例输出
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
保证输入的列表中有且仅有三个数字，且所有数字都是唯一的。
你可以使用三个嵌套的for循环来找出所有可能的排列，但这并不是唯一的方法。
"""
from itertools import permutations
def get_all_permutations(digits):
    # 在此处编写你的代码
    def perm_generator(arr):
        for perm in permutations(arr):
            yield perm

    for perm in perm_generator(digits):
        print(' '.join(map(str, perm)))
        # print(perm)
# 获取整数输入并将其转换为列表
digits = list(map(int, input().split()))
# 调用函数
get_all_permutations(digits)
