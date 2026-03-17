"""
编写一个程序，将一个数字列表按照指定大小分割成特定大小的块。

定义函数list_into_chunks()的函数，有两个参数num_list和chunk_size。
在函数内，将num_list分割成大小为chunk_size的子列表。
将这些子列表作为列表返回。
示例输入
1 2 3 4 5
2
示例输出
[[1, 2], [3, 4], [5]]
解释:
由于测试输入具有奇数个元素，而我们需要创建一个2（偶数）的块大小，剩余的元素将创建一个单元素子列表，即[5]。

输入会包含两行，第一行包含数字并已转为列表，第二行包含块大小。
考虑块大小chunk_size为偶数或奇数的情况。
"""


def list_into_chunks(num_list, chunk_size):
    # 此处编写代码
    return [num_list[i:i + chunk_size] for i in range(0, len(num_list), chunk_size)]

# 从用户输入中获取数据，并将其转换为列表
num_list = list(map(int, input().split()))
# 从用户输入中获取块大小
chunk_size = int(input())
# 调用函数
print(list_into_chunks(num_list, chunk_size))
