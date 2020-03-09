import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-554-9898 Work:212-555-0202')
#print(mo)

xmasRegex = re.compile(r'\d+\s\w+')
mo2 = xmasRegex.findall('12 drummmer, 11 pipers, loards, 9ladies, 8 maids, 7 swans, 6greens')
#print(mo2)

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo3 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD')
print(mo3)