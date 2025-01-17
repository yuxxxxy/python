# 用户名、密码、黑名单

# users = [
#             {
#                 "name" : "小红",
#                 "password" : "123",
#                 "status" : False
#             },
#             {
#                 "name" : "mia",
#                 "password" : "456",
#                 "status" : True
#             },
#             {
#                 "name": "yuxy",
#                 "password": "789",
#                 "status" : True
#             }
#         ]

users = {
            "小红" : {
                "name" : "小红",
                "password" : "123",
                "status" : False
            },
            "mia" : {
                "name" : "mia",
                "password" : "456",
                "status" : True
            },
            "yuxy" : {
                "name": "yuxy",
                "password": "789",
                "status" : True
            }
}


for i in users:
    print(i)


for t in range(3):
    uName = input("请输入你的用户名")
    uPassword = input("请输入你的密码")
    if uName in users and uPassword == users[uName]["password"] and users[uName]["status"]:
        print("登陆成功")
        break
    elif uName in users and not users[uName]["status"]:
        print("你的账户失效了")
    elif uName in users and uPassword != users[uName]["password"]:
        print("你的密码输入错误")
    else:
        print("用户不存在，请先注册！")