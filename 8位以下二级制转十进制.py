def binary_to_decimal(binary_list):
    # 此处编写你的代码
    decimal_value = 0
    for idx, num in enumerate(binary_list):
        decimal_value += num * pow(2, len(binary_list) - 1 - idx)
    return decimal_value


# 获取输入，并转为列表 
binary_list = list(map(int, input().split()))

# 调用函数
print(binary_to_decimal(binary_list))