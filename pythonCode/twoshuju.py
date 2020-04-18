filename = ''
fo = open(filename)
ls = []
for line in fo:
    line = line.replace('\n', '')
    ls.append(line.split(','))
fo.close()

ls = [[],[],[]]
f = open(filename, 'w')
for item in ls:
    f.write(','.join(item) + '\n') 
f.close()
