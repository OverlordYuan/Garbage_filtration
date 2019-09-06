# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import re
import jieba
import opencc
from patten_config import patten

cc = opencc.OpenCC('t2s')

def filter(title='',content='',label=0):
    if title=='' or content=='':
        flag = 1
    else:
        flag = 2
    text = str(title)+str(content)
    for item in patten:
        data_list = re.findall(item, text)
        if len(data_list)>flag:
            label = 1
            break
    return label

def target_fliter(title,content,target,label=0):
    seg_list = list(jieba.cut(cc.convert(title), cut_all=False))
    seg_list += (list(jieba.cut(cc.convert(content), cut_all=False)))
    seg_dict = {}
    for item in seg_list:
        if item in seg_dict.keys():
            seg_dict[item] +=1
        else:
            seg_dict[item] = 1
    if target not in list(seg_dict.keys()) or seg_dict[target]<2:
            label= 1
    return label


