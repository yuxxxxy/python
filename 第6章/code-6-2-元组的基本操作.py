tuple1 = (1,2,3,True,"hello")
print(tuple1)
print(type(tuple1))


tuple2 = (2)
print(type(tuple2))  # 只有一个元素的时候会被去掉一个括号
# 所以只有一个元素的时候我们需要在一个元素后面添加一个逗号
tuple3 = (3,)
print(type(tuple3))
# 一个元素都没有的话用类型转换
tuple4 = tuple()
print(type(tuple4))

tuple5 = tuple("nihaoi")
print(tuple5)
tuple6 = tuple([1,2,3,4])
print(tuple6)
list1 = list(tuple6)
print(list1)
print(type(tuple6),type(list1))

# del,索引,切片,len,max,min,拼接和*，in 和列表一致

# 元组的常用方法
a = tuple5.count("a")
print(a)

b = tuple5.index("i")
print(b)

print("=="*20)
print(tuple6)

# 元组的遍历
for i in tuple5:
    print(i)

for i,j in enumerate(tuple5):
    print(i,j)

for i in range(len(tuple5)):
    print(i,tuple5[i])