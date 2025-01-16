# 除了列表以外最灵活的数据类型
# 列表是有顺序的，列表是没有顺序的
# 键是唯一的，以为键需要当成索引

d = {
    "name":"小明",
    "age":19,
    "gender":True,
    "name":"张三"  # 键重复的话，后者重复的键会覆盖前面的
}
print(d)
print(type(d))

d['height'] = 170  # 新增键值对
print(d)

print(d['gender'])  # 获取键值对

#修改键值对
d['height'] = 180
print(d)
print("张三" in d)  # 只能判断键不能判断value

for i in d:
    print(i,d[i])

print("****"*20)

for k,v in d.items():  # 一般使用这种方法来遍历字典
    print(k,v)

print("****"*20)

for k in d.keys():
    print(k)

print("****"*20)

for v in d.values():
    print(v)

d.pop("gender")
print(d)

a = d.copy()
print("a的键值对",a)
n = a.get('name')
print(n)

print("****"*20)
print(d)
d.popitem()
print(d)
d.clear()
print(d)