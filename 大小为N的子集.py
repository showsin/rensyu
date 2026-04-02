"""
在集合论中，子集是一个数学概念：如果集合A的任意一个元素都是集合B的元素，那么集合A称为集合B的子集。
例如，{1,2,3}是普遍集合{1,2,3,4,5}的子集

编写一个程序来生成给定整数集合的大小为n的所有子集。

定义函数generate_subsets()，有两个参数input_set(整数集合)和n。
在函数内部，生成input_set的大小为n的所有子集，并以列表返回。
示例输入
1 2 3
2
示例输出
[{1, 2}, {1, 3}, {2, 3}]
解释:
{1,2,3}的大小为2的子集为{1,2}，{1,3}和{2,3}

可使用combinations从集合中生成元素组合。
"""
# 从itertools模块中导入combinations函数
from itertools import combinations

# 定义函数
def generate_subsets(input_set, n):
    # 使用combinations生成所有大小为n的组合
    # 注意：combinations需要可迭代对象，所以将集合转换为列表
    return [set(combo) for combo in combinations(input_set, n)]

# 输入整数并将其转换为集合
input_set = set(map(int, input().split()))
# 输入子集大小
n = int(input())
print(generate_subsets(input_set, n))