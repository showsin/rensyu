"""
编写一个程序将字符串从驼峰式写法转换为下划线写法。

定义函数convert_to_snake_case()，接收一个字符串作为参数。
在函数内部，将字符串转换为下划线写法，并返回它。
驼峰式:

骆驼式命名法就是当变量名或函数名是由一个或多个单词连结在一起，而构成的唯一识别字时，第一个单词以小写字母开始；从第二个单词开始以后的每个单词的首字母都采用大写字母，例如：myFirstName、myLastName，这样的变量名看上去就像骆驼峰一样此起彼伏，故得名

下划线写法:

名称中的每一个逻辑断点都用一个下划线来标记，例如：print_employee。下划线命名法是随着C语言的出现流行起来的，在UNIX/LIUNX这样的环境，以及GNU代码中使用非常普遍。

示例输入
firstChallenge
示例输出
first_challenge
"""

def convert_to_snake_case(s):
   # 此处编写代码
    for char in s:
      if char.isupper():
         s = s.replace(char, '_' + char.lower())
    return s
# 获取输入
input_string = input()

# 调用函数，打印输出
print(convert_to_snake_case(input_string))
