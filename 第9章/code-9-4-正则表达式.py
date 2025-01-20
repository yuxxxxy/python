# ids = input("请输入你的身份证号码")
#
# if len(ids) == 18:
#     if(ids[:-1]).isdigit() and (ids[-1].isdigit() or ids[-1] == "X"):
#         print("输入正确")
#     else:
#         print("输入错误")
# else:
#     print("错误")

import re
# a= re.match("hello","hello world")
# print(a)

#检测字符串是否为纯数字的
result = re.match(r"\d+","1234234234")
print(result)

#匹配字符串里的字母数字下划线
result = re.match(r"\w+","123a1*--+234")
print(result)

# \s: 空白字符
# \S: 非空字符
# $表示结尾 ^表示开头
result = re.match(r"\s+","    ss")
print(result)
print("----")
result = re.match(r"^\s+","    ss")
print(result)
print("----")
result = re.match(r"\s+$","    ss")
print(result)

result = re.match(r'^code-\d-\d-\w+$','code-9-3-re')
print(result)

# []区间，可选列表 *和+ 都是表示前面的规则能匹配多少次的意思
# {}里填要精准匹配多少次，可以设定范围如{2，5}
result = re.match(r"^[abcd]$","a")
print(result)

# | 或者的意思
result  = re.match(r"^a|b$","ababab")
print( result)

#匹配身份证号
result = re.match(r"^\d{6}(202[01234]|20[01][01234]|19\d\d)\d{7}(\d|X)$","44522120250421123X")
print(result)


result = re.match(r"^202[01234]$","2022")
result = re.match(r"^20[01]\d$","2022")
print(result)
result = re.match(r"19\d\d","1901")
print(result)


# 手机号码
result = re.match(r"^1\d(10)$","18923413432")
print("手机号",result)