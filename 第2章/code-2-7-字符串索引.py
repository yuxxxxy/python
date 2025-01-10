# 索引
str1 = "hello python"
print(str1[4])
print(str1[-1])
print(str1[0:5])  # 包头不包尾
print(str1[6:8])

str2 = "123456789"
print(str2[0:9:2])  # 每两个取出一个 这一段代码意思是取出0-8位的元素，且步数为2
print(str2[::2])  # 首位可以省略，省略后就默认为从第一个到最后一个

# 字符串反转
print(str2[-1::-1])
print(str2[::-1])