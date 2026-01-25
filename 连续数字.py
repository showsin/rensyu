"""
编写一个程序，判断一个列表中的数字是否可以重新排列成一个连续的数字序列。

定义函数is_consecutive_sequence()，参数为num_list。
在函数内，对列表进行排序。
然后，检查排序后的列表是否形成一个连续的序列，即每两个相邻元素之间的差值是1。
如果序列是连续的，则返回True，否则返回False。
"""

def is_consecutive_sequence(num_list):
    # 此处编写你的代码
    new_list = sorted(num_list)
    continuous_list = [i + min(new_list) for i in range(len(new_list))]
    print(continuous_list)
    return new_list == continuous_list
# 获取输入转为整数列表
nums = list(map(int, input().split()))

# 调用函数
print(is_consecutive_sequence(nums))
