import re
greedyHaRegex = re.compile(r'(ha){3,5}')
mo1 = greedyHaRegex.search('hahahahaha')

print(mo1.group())

print('---------')
nogreedyHaRegex = re.compile(r'(ha){3,5}?')
mo2 = nogreedyHaRegex.search('hahahahaha')

print(mo2.group())