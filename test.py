import jieba
from jieba import analyse
import Spam_Text_Recognition as st
# 引入TextRank关键词抽取接口
textrank = analyse.textrank

jieba.load_userdict("cut_dict.txt")
text = r"埃尔福特是德国中部的一个城市。它是图林根州的首府，并是一个有196,500人口的制造业中心。 埃尔福特东北100公里是莱比锡，向西113公里是卡塞尔和向西北180公里是汉诺威。向外联系则可从慕尼黑转机往埃尔福特机场。 在德国统一之后，埃尔福特是地理上最接近德国中心地带的主要城市。 ​​​".replace('·','')
print(len(text))
temp = list(jieba.lcut(text))
print(temp)
# label = st.Social_media_fliter(text)
