# 集合也是一个没有顺序的数据类型
s = set()
print(s,type(s))

s = {1,2,3,4,5,6,7,1,2,3,4,5}  # 集合的值是不会重复的，有重复的会自动合并掉

print(s)

s = set([1,2,3,4,5,1,2,3])
print(s)

s = set((1,2,3,4,5,6,5,4,3,2,1))
print(s)

s = set("1234")  # 重复执行之后我们就可以发现每一次执行完程序后输出的顺序都是不同的，说明集合是没有顺序的
print(s)

s = set({"name":"张三","age":18})
print(s) #字典转集合，只会取出key而不是value

# 集合是不允许使用索引的 所以运行下一行会报错
# print(s[1])
for i in s:
    print(i)


# 常用的方法
print("****"*20)

print(s)
s.remove('age')
print(s)
s.update({1,2,3,4,5,6,7})
print(s)
s.add("niubi")
print(s)

print("****"*20)

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1,s2)
print(s1 & s2)  # 交集
print(s1 | s2)  # 并集

# 列表去重
score = [80,70,60,80,70,60,40]
s = set(score)
print(s)
d = {}

print("****"*20)
for i in s:
    t = score.count(i)
    d[i] = t

for k,v in d.items():
    print("得分为%d的学生有%d个人" % (k,v))