import random
name = str(input("请输入你的名字："))
times = 0
turns = 0
times_record = []
while True:
    num = random.randint(1,100)
    turns += 1
    while True:
        guessNum = int(input("请输入一个1-100的数字："))
        times += 1
        if guessNum > num:
            print("猜大了，再试试")
        elif guessNum < num:
            print("猜小了，再试试")
        else:
            print("猜对了，你一共猜了" + str(times) + "轮")
            break
    times_record.append(times)
    times_ave = times/turns
    print(name + "你已经完了" + str(turns) + "次，最少" + str(min(times_record)) + "轮猜出答案，平均" + str(times_ave)+ "轮猜出答案")

    game_data = name + " " + str(times) + " " + str(times/turns) + " " + str(min(times_record))
    with open('game_one_user.txt','w') as f:
        f.write(game_data)

    once_more = str(input("是否继续玩游戏？（输入y继续，其他退出）"))
    if once_more == 'y':
        continue
    else:
        print("退出游戏，欢迎下次再来！")
        break

