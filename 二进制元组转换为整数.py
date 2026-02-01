"""
编写一个程序将表示二进制数字的元组转换为整数。

定义函数binary_to_int()，它接受一个参数bin_tuple。
在函数内，将二进制元组转换为十进制整数，并返回结果。
"""


def binary_to_int(bin_tuple):
    # 此处编写代码，bin_tuple 为元组
    return int(''.join(map(str, bin_tuple)), 2)
    # return int(''.join(str(i) for i in bin_tuple), 2)
# 读取输入，将输入转换为元组
bin_tuple = tuple(map(int,input().strip().split()))

# 调用函数binary_to_int()，并输出结果
print(binary_to_int(bin_tuple))