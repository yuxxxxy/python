import math

n1 = 0.1
n2 = 0.2
print(n1+n2)

# 四舍五入
n3 = round(n1+n2,2)
print(n3)

n4 = math.ceil(n1+n2)
print("向上取整的结果是",n4)

n5 = math.floor(n1+n2)
print("向下取整的结果",n5)