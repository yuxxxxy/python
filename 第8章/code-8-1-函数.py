def fun():
    print("helloworld")  # 函数后面一般空两行
def sum1(a,b):
    # print(a + b)
    return a+b


fun()
print(sum1(1,20))

def power(x,n = 2):
    return x**n


print(power(4))
print(power(4,3))

def infos(name,age = 24,gender = "男"):  # 这个就是缺省参数，先给参数一个默认的值，就可以不用传入这个有默认值的参数了
    return "大家好我是%s,我今年%d岁，我是一个%s生" % (name,age,gender)
s = infos("yuxy",21,"男")
lily = infos("lily",gender="女")  # 如果你要不是按顺序的传参数进函数，且参数之间还有缺省参数的话，必须要在有默认参数的实参前添加对应的形参名
print(s)

# 可变参数
def total(*a):  # *a是可变参数，将传入的参数变成tuple
    result = 0
    for i in a:
     result += i
    print(a,type(a))
    return result
result = total(1,2,3,4,5,6,7,8)
print(result)


def f(**kwargs):  #可变参数，接收字典
    for k,v in kwargs.items():
        print(k,v)

d = {"name":"小明","age":18}
f(**d)
