import requests
import time

#下载肖申克的救赎”的电影海报

url = r"https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a"
req = requests.get(url,headers = {"user-agent":"chrome"})
req_json = req.json()
image_url = req_json["image"]
req = requests.get(image_url,headers = {"user-agent":"chrome"})
with open("“肖申克的救赎”的电影海报.jpg","wb") as file :
    file.write(req.content)


#批量获取250部电影的电影名、主演、评分等数据，保存数据到本地 csv 文件

def GetList(start):
    url = "https://api.douban.com/v2/movie/top250?start=%d&apikey=0df993c66c0c636e29ecbb5344252a4a"%start
    req = requests.get(url,headers = {"user-agent":"chrome"})
    req_json = req.json()
    movie_data_list = list()
    NO = 0
    for movie_data in req_json["subjects"] :
        NO += 1
        NO_n = "movie" + str(NO)
        NO_n = [movie_data["id"],movie_data["title"],str(movie_data["rating"]["average"])]
        actor = []
        casts = movie_data["casts"]
        for cast in casts :
            actor.append(cast["name"])
        actor = "，".join(actor)
        NO_n.append(actor)
        NO_n.append(movie_data["images"]["small"])
        movie_data_list.append(NO_n)
    return(movie_data_list)

start = 0
movie_data_list = []
while start<250 :
    movie_20_data_list = GetList(start)
    time.sleep(2)
    start += 20
    movie_data_list += movie_20_data_list
print(movie_data_list)