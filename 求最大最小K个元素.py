"""
编写一个程序，从一个元组中提取最大和最小的K个元素。

定义函数extract_max_min()，有两个参数：input_tuple（一个整数元组）和k（要提取的数量）。
在函数内部，从input_tuple中找到k个最小和k个最大的元素。
返回一个包含提取元素的元组，其中前k个元素是最小的，后k个元素是最大的。
示例输入
4 2 7 9 10 45 3 8
3
示例输出
(2, 3, 4, 9, 10, 45)
解释:
由于测试输入中k的值为3，因此提取并以元组的形式返回最小的3个数（2，3和4）和最大的3个数（9，10和45）

保证k小于等于input_tuple的长度。
"""
# 定义函数
def extract_max_min(input_tuple, k):
    # 对输入元组进行排序
    sorted_tuple = sorted(input_tuple)
    # 在此处编写你的代码
    return tuple(sorted_tuple[:k] + sorted_tuple[-k:])
# 获取整数输入并将其转换为元组
input_tuple = tuple(map(int, input().split()))
# 获取K的值
k = int(input())
# 调用函数
print(extract_max_min(input_tuple, k))