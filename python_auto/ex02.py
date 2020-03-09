import re
beginsWithHello = re.compile(r'Hello')
mo1 = beginsWithHello.search('Hello world')
mo2 = beginsWithHello.search('He said Hello')

print(mo1.group(),mo2.group())

endsWithNumber = re.compile(r'\d$')
mo3 = endsWithNumber.search('Your number is 42')
print(mo3.group())

atRegex = re.compile(r'.at')
mo4 = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo4)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo5 = nameRegex.search('First Name: Al Last Name: Swei')
print(mo5.group(1))

noNewlineRegex = re.compile('.*', re.DOTALL)
mo6 = noNewlineRegex.search('Serve the public trust. \nProduct the innocent. \nUpload the law.')
print(mo6.group())