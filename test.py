import jieba
jieba.load_userdict("cut_dict.txt")
text0 = r"换装1.5T，搭载大屏，五菱宏光也要高端化？网友：这辈子不可能了"
# text = "中国护照免签又多了一个国家！ 9月12日，乌兹别克斯坦总统米尔济约耶夫签署法令，规定自2020年1月1日起，包括香港特别行政区在内的中国公民可通过该国国际机场免签进入乌兹别克斯坦，停留不超过7天。"
temp = list(jieba.cut(text0))
print(temp)
# import re
# from patten_config import patten
# text = '【顺联动力】【新车定金】奥迪A3 2019款 Sportback 35 TFSI 进取型 汽车整车O网页链接 ​'
# data_list = re.findall(patten[0], text)
# # if len(data_list)>2:
#
# for item in patten[1]:
#     text = re.compile(item).sub('', text)
# print(text)