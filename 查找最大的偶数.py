def find_largest_even(lst):
    # 此处编写你的代码

    a = [char for char in lst if char%2==0]
    if a:
        return max(a)
    else:
        return -1


# 获取输入转为整数列表
input_list = list(map(int, input().split()))

# 调用函数
print(find_largest_even(input_list))