# 题目要求：输入2024-02-25，输出这一天是这一年的第多少天
date = input("请输入日期：")
year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])
is_run = False
sum_day = 0

print("年：%s月：%s日：%s" % (year,month,day))

# 存大月
big_month = [1,3,5,7,8,10,12]

# 判断闰年
if year % 4 == 0:
    is_run = True
    if year % 100 == 0:
        is_run = False
        if year % 400 == 0:
            is_run = True

# 先循环从1月到输入的月份
for i in range(1,month):
    # 判断是否是大月
    if i in big_month:
        sum_day += 31
    # 判断是是否是闰年还是平年，来决定2月是28天还是29天
    elif i == 2:
        if is_run:
            sum_day += 29
        else:
            sum_day += 28
    # 如果是小月就正常的加30天就行了
    else:
        sum_day += 30
    print(sum_day)

print("****"*40)

# 再加上最后一个月的天数
sum_day += day

print(sum_day)