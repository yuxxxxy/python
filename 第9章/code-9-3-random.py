import random

#随机数
a = random.random()
print(a)
b = random.randint(1,100)
print(b)

list1 = [1,2,3,4,5,6,7]
print(list1[random.randint(0,len(list1)-1)])
print(random.choice(list1))
print(random.choice("nihao"))

# 生成一个随机字母组成的列表
c = []
print(ord("A"),ord("Z"))
for i in range(20):
    s = ''
    for j in range(5):
        t = random.randint(65,90)
        s += chr(t)
    c.append(s)

print(c)

random.shuffle(list1)
print(list1)