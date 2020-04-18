def prime(n):
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1
    return flag
n = eval(input())
a = int(n)
a = a + 1if a < n else a

counter = 5
t = ''
while counter > 0:
    if prime(a) == 0:
        print(a)
        counter -= 1
    a += 1