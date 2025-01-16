# range 生成一个等差数列
# range(start,end,[step = 1]) step是步数默认为1 start 默认为0 stop表示结束值，但是不包含
# range 的参数是一个左闭右开的

for i in range(10):
    print(i,end=" ")

print("\n")

for j in range(2,10):
    print(j,end=" ")

print("\n")

for k in range (2,10,3):
    print(k,end=" ")

total = 0
for i in range(1000,10001):
    total += i

print(total)

# 水仙花数

# 每一位数字的立方和 = 三位数本身
for i in range(100,1000):
    a = i%10
    b = i // 10 % 10
    c = i // 100
    total = a*a*a + b*b*b + c*c*c
    if total == i:
        print(i)