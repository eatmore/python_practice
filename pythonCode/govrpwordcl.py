# govrpwordcl.py
import jieba
import wordcloud
from imageio import imread
f = open('新时代中国特色社会主义.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
mask = imread('timg.png')

ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path='simhei.ttf', width=1000, height=800, mask=mask,background_color='white')

w.generate(txt)
w.to_file('grwordcloud2.png')