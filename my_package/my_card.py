from Tools.scripts.win_add2path import modify

cards = [{"name": "jack","phone":"123", "qq": "QQHAO1","email":"123@QQ.COM"},
         {"name": "LIHUA","phone":"1234", "qq": "QQHAO2","email":"456@QQ.COM"},
         {"name": "TT","phone":"12345", "qq": "QQHAO3","email":"789@QQ.COM"}]

def menu():
    print("*"*30)
    print("""欢迎使用名片管理系统
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统""")
    print("*" * 30)

def new_card(name,phone,qq,email):
    user = {"name":name,"phone":phone,"qq":qq,"email":email}
    cards.append(user)
    print("名片新建成功！")
    return True

def show_card():
    for i in cards:
        for k,v in i.items():
            print(k,v)
        print("----"*10)


def query_card(kw):
    for i in cards:
        for k,v in i.items():
            if kw == v:
                return i

def modify_card(card):
    temp = card
    temp["name"] = input("姓名:")
    temp["phone"] = input("手机号:")
    temp["qq"] = input("qq:")
    temp["email"] = input("邮箱号:")
    cards[cards.index(card)] = temp

def del_card(card):
    cards.remove(card)

def quit():
    print("系统已退出")


def start():
    menu()

    while True:
        op = input("请输入你想要的操作的序号")
        if op == "1":
            name = input("姓名:")
            phone = input("手机号:")
            qq = input("qq:")
            email = input("邮箱号:")
            result = new_card(name,phone,qq,email)

            menu()
        elif op == "2":
            show_card()
            menu()
        elif op == "3":
            kw = input("请输入关键字:")
            result = query_card(kw)
            if result:
                op2 = input("输入4进行修改名片，输入5进行删除")
                if op2 == "4":
                    modify_card(result)
                    print("修改成功")
                elif op2 == "5":
                    del_card(result)
                    print("删除成功")
            else:
                print("未查到有该信息的名片")
            menu()
        elif op == "0":
            quit()
            break
        else:
            print("请重试")