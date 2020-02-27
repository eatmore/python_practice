import random
while True:
    times = 0
    a = random.randint(1, 100)
    while True:
        b = int(input("请猜一个1-100的数字："))
        times += 1
        if a > b:
            print("猜小了，再试试")
        elif a < b:
            print("猜大了，再试试")
        else:
            print("猜对了，你一共猜了" + str(times) + "轮")
            break
    once_more = str(input("是否继续游戏？输入y继续，其他退出"))
    if once_more == "y":
        continue
    else:
        print("退出游戏，欢迎下次再来！")
        break