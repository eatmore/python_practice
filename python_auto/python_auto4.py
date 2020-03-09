import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search("The Adventures of Batman")
#print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowoman')
#print(mo3.group())

heRegex = re.compile(r'(ha){3}')
mo4 = heRegex.search('hahaha')

print(mo4.group())

hoRegex = re.compile(r'ho{3}')
mo5= hoRegex.search('hooo')

print(mo5.group())