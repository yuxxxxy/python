from operator import is_not

print("12" in "123")
print("hi" in "hello")

# 布尔值和浮点数不能用成员运算符

a = "nihao"
b = "nihaoa"
print(a is b)
b = "nihao"
print(a is b)
print(a is not b)
print("-----------------------")
print('python'<'pyti')
print('ABCD' == 'abcd'.upper())
print('python123'>'python')
print(''<'a')