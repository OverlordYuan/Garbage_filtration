# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/9/04
"""
import pandas as pd
import os
filename = '华为_garbage_2019-09-05_14_32'
data =pd.read_csv('output/华为/'+filename+'.csv',index_col=0)
print('垃圾文本数量为:{}'.format(data.shape[0]))
type = list(set(data['source'].tolist()))
# print(type[0])
path = 'output/sample/' + filename
if not os._exists(path):
    os.mkdir(path)
for item in type:
    data_temp = data[data['source'].isin([item])]
    print('{}垃圾文本数量为:{}'.format(item,data_temp.shape[0]))
    if data_temp.shape[0]>100:
        temp = data_temp.sample(n=100)
        temp.to_csv(path+'/'+item+'_garbage_'+str(data_temp.shape[0])+'sample_100.csv',encoding='utf-8-sig')
    else:
        data_temp.to_csv(path+'/'+item+'_garbage_'+str(data_temp.shape[0])+'sample_'+str(data_temp.shape[0])+'.csv',encoding='utf-8-sig')
    # print(data_temp.shape)
# data1 = data[data['source'].isin(['微博'])]
# data.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)