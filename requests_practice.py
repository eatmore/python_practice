import requests

r = requests.get('http://www.baidu.com')

print(r.status_code)
print(r.text)
print(r.encoding)
print(r.apparent_encoding)
r.encoding = 'utf-8'

print(r.text)

try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
except:
    return '产生异常'