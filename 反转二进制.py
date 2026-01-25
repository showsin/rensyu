"""
编写一个程序，输入一个正整数，将其转换为二进制，然后反转二进制字符串，最后返回反转后的二进制字符串对应的十进制数。

定义函数reverse_binary_integer()，参数为一个整数。
在函数内，将整数转换为二进制表示，反转二进制字符串，然后将其转换回十进制。
返回最后的十进制数。
"""



def reverse_binary_integer(n):
    # 此处编写你的代码
    bi = bin(n)
    re_bi = str(bi)[:1:-1]
    int_num = int(re_bi, 2)
    return int_num
# 获取输入
n = int(input())

# 调用函数
print(reverse_binary_integer(n))