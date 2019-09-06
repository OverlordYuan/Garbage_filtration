# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import os
import pandas as pd
import datetime
import jieba
import opencc
import Spam_Text_Recognition as pf
from tqdm import tqdm

cc = opencc.OpenCC('t2s')

class Spam():
    def __init__(self,target):
        '''
        本地测试垃圾识别初始化程序
        :param target: 识别的主题及文件的路径
        '''
        self.root_dir = os.path.abspath('.')
        self.input_dir = os.path.join(self.root_dir,'input')
        self.output_dir = os.path.join(self.root_dir,'output')
        self.target = target

    def read_xls(self):
        data_pd = pd.DataFrame(columns=['title','content','source','label'])
        # data_pd = pd.DataFrame()
        data_dir = os.path.join(self.input_dir,self.target)
        list = os.listdir(data_dir) #列出文件夹下所有的目录与文件
        for i in range(0,len(list)):
            if os.path.splitext(list[i])[1] == ".xls" or  os.path.splitext(list[i])[1] == ".xlsx":
                path = os.path.join(data_dir,list[i])
                if os.path.isfile(path):
                    print(i)
                    sheet = pd.read_excel(path)
                    if i == 0:
                        data_pd['title'] = sheet['标题']
                        data_pd['content'] = sheet['内容']
                        data_pd['source'] = sheet['渠道']
                        type = set(data_pd['source'].tolist())
                        print(type)
                    else:
                        data_temp = pd.DataFrame()
                        data_temp['title'] = sheet['标题']
                        data_temp['content'] = sheet['内容']
                        data_temp['source'] = sheet['渠道']
                        data_pd = pd.concat([data_pd,data_temp],ignore_index=True,sort=False)
                        type = set(data_pd['source'].tolist())
                        print(type)
        return data_pd

    def read_csv(self):
        data_dir = os.path.join(self.input_dir, self.target)
        list = os.listdir(data_dir)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            if os.path.splitext(list[i])[1] == ".csv":
                path = os.path.join(data_dir, list[i])
                data_pd = pd.read_csv(path,index_col=0)
                return data_pd

    def save_rusult(self,data_pd):
        time = str(datetime.datetime.now()).replace(' ','_').split(':')
        label =time[0]+'_'+time[1]
        data_dir = os.path.join(self.output_dir, self.target)
        try:
            data_pd_dir = os.path.join(data_dir, self.target+'_data_'+label+'.csv')
            garbage_pd_dir = os.path.join(data_dir, self.target+'_garbage_'+label+'.csv')
            data = data_pd[data_pd['label'].isin([0])]
            Garbage = data_pd[data_pd['label'].isin([1])]
            print(Garbage.shape)
            data.to_csv(data_pd_dir, encoding='utf-8-sig')
            Garbage.to_csv(garbage_pd_dir, encoding='utf-8-sig')

        except Exception as e:
            print(e)
            print('Save failed!')

    def target_fliter(self,title,content,label=0):
        seg_list = list(jieba.cut(cc.convert(title), cut_all=False))
        seg_list += (list(jieba.cut(cc.convert(content), cut_all=False)))
        seg_dict = {}
        for item in seg_list:
            if item in seg_dict.keys():
                seg_dict[item] +=1
            else:
                seg_dict[item] = 1
        if self.target not in list(seg_dict.keys()) or seg_dict[self.target]<2:
                label= 1
        return label

    def Garbage_analysis(self,data):
        data_len = data.shape[0]
        data['label'] = [0]*data_len
        for i in tqdm(range(data_len)):
            try:
                try:
                    title = data['title'][i]
                except:
                    title = ''
                try:
                    content =  data['content'][i]
                except:
                    content = ''
                # if data['source'][i] =='电子报纸' or data['source'][i] =='网站' or data['source'][i] =='APP':
                #     data['label'][i] =self.target_fliter(title, content, 0)
                # else:
                #     data['label'][i] = pf.filter(title,content,0)
                if data['source'][i] == '微博':
                    data['label'][i] = pf.filter(title, content, 0)
                elif len(str(content))>200:
                    data['label'][i] =self.target_fliter(title, content, 0)
                else:
                    data['label'][i] = pf.filter(title,content,0)
            except Exception as e:
                print(e)
        return data
