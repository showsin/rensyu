"""
编写一个程序来检查是否可以重新排列给定的单词字母来形成回文单词。
回文是一个从前往后和从后往前读都一样的字符串，例如pop，racecar等。

定义函数can_form_palindrome()的函数，参数为word(即输入的单词)。
在函数内，如果输入字符串可以重新排列以形成回文，则返回True，否则返回False。
示例输入
sarars
示例输出
True
解释:
可以重新排列sarars字母形成回文单词rassar。
"""
def can_form_palindrome(word):
    # 在此处编写你的代码
    char_count = {char: word.count(char) for key, char in enumerate(word)}
    return sum(count % 2 for count in char_count.values()) <= 1

# 从用户处获取输入
word = input()
# 调用函数
print(can_form_palindrome(word))