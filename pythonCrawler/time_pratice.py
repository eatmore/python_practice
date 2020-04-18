import requests, time
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")

url = 'https://www.baidu.com/'
start = time.perf_counter()
for i in range(100):
    c = get_html(url)
    if c == "爬取失败":
        print("第{}次爬取{}".format(i+1, c))
end = time.perf_counter()
print("爬取100次花费时间:{}".format(end - start))