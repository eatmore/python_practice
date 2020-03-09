import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo =phoneNumRegex.search('My number is: 415-554-4242.')
#print(mo.group(1))
#print(mo.group(0))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)