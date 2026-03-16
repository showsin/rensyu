"""
编写一个程序来检查给定的数字是否可以表示为两个或多个连续正数的和。

例如:

1 + 2 +3 = 6
4 + 5 = 9
其中6 和 9 均可以表示为连续数字的和。

定义函数check_consecutive_sum()，参数为n。
在函数内，检查该数字n是否可以表示为连续数字的和。
如果该数字可以表示为连续数字的和，则返回True，否则返回False。
示例输入
6
示例输出
True
解释:
1，2和3是连续的数字，加起来等于6。
"""


def check_consecutive_sum(n):
    # 此处写代码
    return (n & (n - 1)) != 0
# 获取输入数字n
n = int(input())

# 调用函数
print(check_consecutive_sum(n))