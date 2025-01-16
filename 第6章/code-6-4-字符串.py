s1 = "hello world   "
print(s1)
print(s1+"yuxy")
print(s1*3)


s2 = "NIUBI"
s3 = "niuBI"
print(s1.islower())  # 检测字符串是不是全部都是小写的
print(s2.isupper())  # 检测字符串是不是全部都是大写的
print("****"*10)
print(s3.isupper())
print(s3.islower())


print(s1.strip())  # 去除字符串后面的空格
print(s1)
print(s1.split(' '))

print(' '.join(s2))  # 为字符串中的每个元素添加一个连接符

s = input("请输入一篇文章")
a,b,c = 0,0,0
for i in s:
    if i.isalpha():
        a += 1
    elif i.isdigit():
        b += 1
    else:
        c += 1
print("字母：%d,数字：%d,符号%d" % (a,b,c))