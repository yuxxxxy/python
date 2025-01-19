import random

# 石头剪刀布
def game(round):
    p_win = 0
    c_win = 0
    for i in range(round):
        player = input("请输入石头剪刀布:")
        computer = random.choice(["石头","剪刀","布"])
        if(player == computer):
            print("这回合平局")
        elif((player == "石头" and computer == "剪刀") or (player == "布" and computer == "石头") or (player == "剪刀" and computer == "布")):
            p_win += 1
            print("这回合你赢了")
        else:
            c_win += 1
            print("这回合你输了")
    print("====="*10)
    if p_win >=2:
        print("你赢了")
        return True
    elif p_win == c_win:
        print("平局")
    else:
        print("你输了")
        return False

# game(3)


#猜数字
def guess_num():
    num = random.randint(1,100)
    min_num = 1
    max_num = 100
    time = 1
    while True:
        player = int(input("请输入数字:"))
        if player == num:
            print("猜中了！！！\n你使用了%d次就猜中了" % time)
            return True
        elif player > num and player < max_num:
            max_num = player
            print("猜大了!范围是%d-%d"%(min_num, max_num))
        elif player < num and player > min_num:
            min_num = player
            print("猜小了!范围是%d-%d" % (min_num, max_num))
        elif player > max_num or player < min_num:
            print("你的输入有误请重新输入")
            continue
        time += 1

guess_num()