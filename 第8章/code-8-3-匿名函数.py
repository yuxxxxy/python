from functools import reduce


# def sum1(a,b):
#     return a+b
#
# a = sum1(1,2)
# print(a)
#
# c = lambda a,b:a+b  # 创建匿名函数
# print(c(1,2))  # 省略了创建函数的过程

a = [1,2,3,4,5]
result = []
for i in a:
    result.append(i**2)
print(result)

b = [1,2,3,4,5]
for i in range(len(b)):
    b[i] = b[i]**2
print(b)



c = [1,2,3,4,5]

# def f(x):
#     return x**2
#
# result = map(f,c)  # map函数使用来做映射的，将第二个参数的内容拿出来，放到第一个参数里面去进行操作

result = map(lambda x:x**2,c)

print(list(result))

# reduce 累计\累加  将c中每个元素取出来和下一个取出来的元素执行第一个参数的运算
result = reduce(lambda x,y:x+y,c)
print(result)

# filter 过滤 第一个参数是过滤的条件
result = filter(lambda x:x%2==0,c)
print(list(result))

print("===="*10)

d = [1,2,3,4,5,6,7,0,8,0,9,0]
result = filter(lambda x:x!=0,d)
print(list(result))

result = int(reduce(lambda x,y:str(x)+str(y),d))
result2 = reduce(lambda x,y:x*10**len(str(y))+y,d)
print(result,type(result))
print(result2,type(result2))