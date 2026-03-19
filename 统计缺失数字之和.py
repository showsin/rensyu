"""
编写一个程序来统计缺失的数字并返回它们的总和。
缺失的数字是指给定列表中两个极端（最大和最小数字）之间没有出现的数字。

例如，在列表[2, 5, 3, 7]中，两个极端（即2和7）之间缺失的数字是4和6。

定义函数missing_numbers_info()的函数，参数为num_list。
在函数中，返回一个元组，元组中有两个元素：缺失数字的数量和它们的总和。
如果没有缺失的数字，则返回**(0, 0)**。
示例输入
5 2 7 3
示例输出
(2, 10)
解释:
在测试输入中，2是最小的，7是最大的元素。在这之间，除了4和6之外，列表中的所有元素都存在。它们的总和是10。因此，我们的输出是**(2,10)**
"""

def missing_numbers_info(num_list):
    # 此处写下你的代码
    num_list.sort()
    num_count = 0
    num_sun = 0
    for num in range(num_list[0], num_list[-1]):
        if num not in num_list:
            num_count += 1
            num_sun += num
    return (num_count, num_sun)
# 获取整数输入并将其转换为列表
num_list = list(map(int, input().split()))
# 调用函数
print(missing_numbers_info(num_list))