f = open('data.csv', 'r')
lst = f.readlines()
lst = lst[::-1]
lt = []
for item in lst:
    item = item.strip('\n')
    item = item.replace(' ', '')
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close()