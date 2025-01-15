age = [18, 20, 19]
print(type(age))
sum = 0
for i in range(len(age)):
    sum += age[i]
print(sum / len(age))


list2 = list()  # 类型转换：把参数转化成列表 会把参数一个一个拆开添加进列表
print(type(list2))
list3 = list("123456789")
print(list3)
print(type(list3[0]))


# 切片
print(list3[::2])
print(list3[::-2])



# 列表加法

list4 = age + list3
list5 = list3 + age
print(list4)
print(list5)

print(19 in age)
print(19 in list3)
print(1  in list3)
print(1 not in list3)  # list3 里存储的都是str

print([1,2,3,4] < [3,4])
print([4,2,3,4] < [3,4])

# 内置函数 函数名()
print(len(list3))
print(min(list3))
print(max(list3))
# del list3
# print(list3)  # 运行报错显示是list3 not defined说明已经生效了

# 列表的遍历
list3 = list("123456789")
for i in list3:
    print(list[i])

for i,j in enumerate(list3):  # 枚举
    print(i,j)  # 带着索引输出


# 列表的常用方法 变量.方法名()

list3.append("nihao")  # 添加的是一个元素
print(list3)

list3.extend(["hhaha", "woniubi"])  # 添加的是一个列表
print(list3)

list3.insert(3,"wochao_insert")
print(list3)

print("=="*15)
list3.pop(9)
print(list3)

list3.remove("wochao_insert")  # remove是按值来删除
print(list3)

list3.append("nihao")
print(list3)
list3.remove("nihao")  # remove删除从前面开始找，删除第一个匹配的
print(list3)

age.clear()  # 清空列表
print(age)

age = list3.copy()  # 复制
print(age)