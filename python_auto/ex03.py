import re
robocop = re.compile(r'robocop', re.I)
mo1 = robocop.search('PRobocop is part man, part machine, all cop.')

#print(mo1.group())

namesRegex = re.compile(r'Agent \w+')
mo2 = namesRegex.sub('CENSORED', 'Agent Alisce gave the secret documents to Agent Bob.')

print(mo2)

phoneRegex = re.compile(r'''(
    (\d{3}|(\d{3}\))?  # area code
    (\s|-|\.)?   # separator

)'''.re.VERBOSE)

somesRegexValue = re.compile('foo', re.IGNORECASE|re.DOTALL|re.VERBOSE)