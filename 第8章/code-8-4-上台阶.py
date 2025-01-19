sum = 0


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n-2) + f(n-1)

for i in range(11):
    print("%d阶楼梯有%d种走法" % (i,f(i)))

print("====="*10)

a = [0,1,2]
for i in range(3,11):
    a.append(a[i-1]+a[i-2])
    print("%d阶楼梯有%d种走法" % (i,a[i]))

# 不建议使用递归的方法解决，因为递归的方法效率非常的低