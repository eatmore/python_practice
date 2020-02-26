import random
a = random.randint(1, 100)
print(a)
n = 0
while True:
    b = int(input("请猜一个1-100的数字："))
    n += 1
    if a > b:
        print("猜小了，再试试")
    elif a < b:
        print("猜大了，再试试")
    else:
        print("猜对了，你一共猜了" + str(n) + "轮")
        break