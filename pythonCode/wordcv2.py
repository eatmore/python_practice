import jieba
import wordcloud

txt = '明月几时有把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间'
w = wordcloud.WordCloud(width=1000, height=800)
print(jieba.lcut(txt))
w.generate(' '.join(jieba.lcut(txt)))
#w.to_file('wordcl.png')