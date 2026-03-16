"""
编写一个程序来验证一个邮箱地址是否合法。

定义函数is_email_valid()，参数为email。
在函数内，如果邮箱email满足下面提到的条件，则返回True，否则返回False。
要求邮箱有效，必须满足以下条件：

字符串必须包含一个@字符。
字符串必须包含一个.字符。
@必须有至少一个字符在它之前。
.和@必须处于适当的位置。
例如，hello.email@com是无效的，而john.smith@email.com是有效的。

示例输入
user@website.com
示例输出
True
解释:
测试输入user@website.com返回True，因为它满足程序中指定的有效邮箱地址的所有条件。
"""

import re

def is_email_valid(email):
    # 此处编写代码
    pattern = r'^[^@]+@[^@.]+\.+[^@.]+$'
    return bool(re.match(pattern, email))# 获取输入
email = input()

print(is_email_valid(email))