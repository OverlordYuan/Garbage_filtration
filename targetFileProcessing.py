# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/9/16
"""
import pandas as pd
import pickle

data = pd.read_csv('input/汽车品牌知识库.csv', encoding = 'gb2312',index_col='序号')
temp0 = data['品牌'].tolist()
temp0 = list(set(temp0))
temp0.remove('北京')
temp0.remove('上海')
temp0.remove('谷歌')
aa = []
for item in temp0:
    if len(item)==2:
        aa.append(item+'车')
temp0 = temp0+aa
temp1 = data['品牌分类'].tolist()
temp2 = data['汽车型号'].tolist()
temp = temp0+temp1+temp2
data_list = (list(set(temp)))
# print(len(data_list))
data_list.append('汽车')
data_list.append('新能源汽车')
data_list.append('梅赛德斯')
data_list.append('北汽')
data_list.append('一汽')
data_list.append('上汽')
data_list.append('广汽')
data_list.append('福汽')
data_list.append('一汽大众')
data_list  = list(map(lambda x:x.upper(),data_list))
print(len(data_list))
with open('targets.txt', 'wb') as f:
    pickle.dump(data_list, f, pickle.HIGHEST_PROTOCOL)
