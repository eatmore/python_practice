import requests
import os
root = '/Users/wangyanjun/Downloads'
url = 'https://img1.doubanio.com/view/photo/raw/public/p2587350708.jpg'

try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url, headers = {"user-agent":"chrome"})
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')