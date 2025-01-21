import time

t = time.time()
print(t)

t = time.localtime()
print(t)

print(t.tm_year,type(t.tm_year))

s = time.strftime("%H:%M:%S",t)
