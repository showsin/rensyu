"""
编写一个程序，检查列表是否存在两数字之和等于给定的数。

定义函数is_sum_present()，它接受两个参数 - 一个数字列表num_list和一个数字target_sum。
在函数内，检查列表中的每对数字。如果任意一对数字的和等于target_sum，则返回True。否则，返回False。

示例输入
2 3 7 8 11
14

示例输出
True

解释:
由于我们的目标数是14，而我们列表中的[11, 3]是两个数字，它们相加等于14，因此输出为True。
"""


def is_sum_present(num_list, target_sum):
    # 此处编写代码
    senn = set()
    for num in num_list:
        if target_sum - num in senn:
            return True
        senn.add(num)
    return False
# 获取输入
num_list = list(map(int, input().split()))
target_sum = int(input())

# 调用函数
print(is_sum_present(num_list, target_sum))