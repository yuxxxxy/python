
while True:
    try:
        op = input("请输入一个四则运算算式(例如 1 + 2):\n")
        result = 0

        if "+" in op:
            a = op.split("+")
            result = int(a[0]) + int(a[1])
        elif "-" in op:
            a = op.split("-")
            result = int(a[0]) - int(a[1])
        elif "*" in op:
            a = op.split("*")
            result = int(a[0]) * int(a[1])
        elif "/" in op:
            a = op.split("/")
            result = int(a[0]) / int(a[1])
        elif op == "C":
            print("感谢使用")
            break
        else:
            raise Exception("请1+2这个格式输入算式！")
        print(result)
    except ZeroDivisionError:
        print("出发运算，除数不能为0")
    except Exception as e:
        print(e)


