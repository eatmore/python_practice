f = open('latex.log')
s, n = 0,0
for line in f:
    line = line.strip('\n')
    if line == '':
        continue
    s += len(line)
    n += 1
print(round(s / n))
