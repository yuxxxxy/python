# 全局变量
num1 = 1

def demo1():
    num2 = 2  # 局部变量
    num1 = 8  # 重新定义一个和全局便改良同名的num1
    print(num1)

demo1()
print(num1)
# print(num2)  # num2 是局部变量所以无法打印，报错是num2没有给定义

def demo2():
    global num1  # 声明num1和外部全局变量是同一个变量
    print(num1)
    num1 = 20  # 函数内修改

demo2()
print(num1)  # 看一下可以发现num1给修改了