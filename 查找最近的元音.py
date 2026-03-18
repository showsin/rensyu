"""
编写一个程序，查找给定字母最近的元音。

定义函数closest_vowel()，参数为一个字母letter。
在函数内，确定给定字母最近的元音。
如果两个元音离给定字母距离相等，则返回字母顺序较小的元音。
另外忽略字母大小写，将输入的字母转换为小写。

示例输入
f
示例输出
e
解释:
由于e是f最近的元音，因此它是此测试输入用例的输出。

元音字母为a、e、i、o、u。
"""

def closest_vowel(letter):
    # 此处编写代码
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter = letter.lower()
    vowel_distance = []
    for vowel in vowels:
        distance = abs(ord(letter) - ord(vowel))
        vowel_distance.append((distance, vowel))

    vowel_distance.sort()

    return vowel_distance[0][1]

# 获取输入
letter = input()
# 调用函数
print(closest_vowel(letter))