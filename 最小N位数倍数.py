"""
编写一个程序，找出最小的N位数字，满足指定值的倍数。

定义函数smallest_multiple()，有两个参数，digits（即N）和multiple_of（整数）。
在函数内，返回最小的N位数数字，它是指定值的倍数。
这里，digits是数字的位数(即N)，目标值应该是multiple_of的倍数。

示例输入
4
6
示例输出
1002

解释:
最小的4位数1002是6的倍数。
"""

def smallest_multiple(digits, multiple_of):
    # 此处编写代码
    start = 10 ** (digits - 1)
    result = ((start + multiple_of - 1) // multiple_of) * multiple_of
    if result < 10 ** digits:
        return result
    else:
        return  False
# 获取输入
digits = int(input())
multiple_of = int(input())

# 调用函数，输出结果
print(smallest_multiple(digits, multiple_of))