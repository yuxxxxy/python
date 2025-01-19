import random

def random_char(upper=True):
    if upper:
        t = random.randint(ord("A"), ord("Z"))
        return chr(t)
    else:
        t = random.randint(ord("a"), ord("z"))
        return chr(t)

def random_str(length):
    s = ""
    for i in range(length):
        s += random_char(random.choice([True,False]))
    return s

def yzm(length):
    return random_str(length)

def main():
    # a = []
    # for i in range(20):
    #     a.append(random_str(random.randint(3,6)))
    # return a
    print(yzm(5))
main()
# print(main())