import requests
url = 'http://httpbin.org/get'
h = {
    'host':'httpbin.org',
    'user-agent':'chrome v70',
    'cookie': 'id=123; some_cookie_info'
}
r = requests.get(url, headers=h)
print(r.text)