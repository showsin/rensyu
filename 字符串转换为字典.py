"""
编写一个程序将字符串转换为字典。

定义函数convert_str_list_to_dict()，参数为str_list(输入的字符串)。
在函数内部，创建一个字典，其中每个字符串使用=进行分割，第一部分为键，第二部分为值。
返回字典。
示例输入
5=Five 6=Six 7=Seven
示例输出
{'5': 'Five', '6': 'Six', '7': 'Seven'}
"""

def convert_str_list_to_dict(str_list):
    # 此处编写代码
    # return {key: value for key, value in (item.split('=') for item in str_list.split())}
    return dict(item.split('=') for item in str_list.split())
# 输入字符串
str_list = input()

# 调用函数
print(convert_str_list_to_dict(str_list))