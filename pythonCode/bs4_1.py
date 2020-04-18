import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
r.text
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
#print(soup.prettify())
print(soup.title)
print(soup.a)
tag = soup.a
print(tag.attrs)
print(tag.attrs['class'])
print(soup.p)