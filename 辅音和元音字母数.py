"""
编写一个程序来计算给定单词中辅音字母和元音字母的数量。

定义函数count_consonants()，参数为word。该函数应返回单词中辅音字母的数量。
定义函数count_vowels()，参数为word。该函数应返回单词中元音字母的数量。
"""

def count_consonants(word):
    # 在此处编写你的代码
    list_con = [i for i in word if i.isalpha() and i not in 'aeiouAEIOU']
    return len(list_con)
def count_vowels(word):
    # 在此处编写你的代码
    list_vow = [i for i in word if i.isalpha() and i in 'aeiouAEIOU']
    return len(list_vow)
# 获取用户输入
word = input()

# 调用函数
print(count_consonants(word))
print(count_vowels(word))