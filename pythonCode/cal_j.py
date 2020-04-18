'''enerTra = input()
if enerTra[-1] in ['J', 'j']:
    CalResult = (eval(enerTra[0:-1]))/4.186
    print('{:.3f}cal'.format(CalResult))
elif enerTra[-3:-1].lower() in ['cal']:
    JoReslut = (eval(enerTra[0:-3])) * 4.186
    print('{:.3f}J'.format(JoReslut))
else:
    print('输入错误')'''

print('22.345cal'[0:-3])
print('22.345cal'[-3:-1])