from logging import exception

try:
    pwd = input("请输入你的密码")
    if len(pwd) < 8:
        raise Exception("密码的长度需要到8位以上")
except Exception as e:
    print(e)