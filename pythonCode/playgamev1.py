from random import random
def printInfo():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0-1之间的小数表示）')

def getInputs():
    a = eval(input('请输入选手A的能力值（0-1）：'))
    b = eval(input('请输入选手B的能力值（0-1）：'))
    n = eval(input('模拟比赛的场次'))
    return a, b, n

def printSummary(wishA, wishB):
    n = wishA + wishB
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(wishA, wishA/n))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(wishB, wishB/n))

def simNGames(n, proA, proB):
    wishA, wishB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneNGame(proA, proB)
        if scoreA > scoreB:
            wishA += 1
        else:
            wishB += 1
    return wishA, wishB

def gameOver(a,b):
    return a == 15 or b == 15

def simOneNGame(proA, proB):
    scoreA, scoreB = 0, 0
    serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < proA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < proB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB

def main():
    printInfo()
    proA, proB, n = getInputs()
    wishA, wishB = simNGames(n, proA, proB)
    printSummary(wishA, wishB)

main()