for i in range(1000, 10000):
    a = int(str(i)[0])
    b = int(str(i)[1])
    c = int(str(i)[2])
    d = int(str(i)[3])
    n = pow(a,4) + pow(b,4) + pow(c,4) + pow(d,4)
    if n == i:
        print(i)