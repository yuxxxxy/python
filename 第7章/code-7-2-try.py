# try:
#     # print("可能出现异常的代码")
#     # a = 1 + "2"
#     n = int(input("输入一个数字"))
#     sum = 5.0 / n
#     print(sum)
# except:
#     print("如果出现了异常，会执行这个代码块")
# finally:
#     print(" ")
#     # print("不管如何都会执行")
#     # print("这里面一般放着关闭数据库或者清理内存之类的代码，保证资源的不浪费")


try:
    n = int(input("请输入一个数字"))
    n = 5 / n
    print(n)
except ZeroDivisionError as e:  # as是用于创建一个别名，或者为变量添加一个标签，以便于更加方便的处理变量和处理变量
    print("原始报错信息",e)
    print("除数不能为 0")
except:
    print("请输入一个数字")
else:  # 报错的时候不进入else模块，只有运行时没有被except模块捕获，执行else模块
    print("进入else模块")
finally:  # 无论如何都会执行finally模块
    print("进入finally模块")