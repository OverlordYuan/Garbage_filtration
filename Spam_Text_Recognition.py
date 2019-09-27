# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import re,pickle
import jieba
import opencc
from patten_config import patten
import jieba.analyse
jieba.load_userdict("cut_dict.txt")
cc = opencc.OpenCC('t2s')
with open('targets.txt', 'rb') as f:
    targets = pickle.load(f)

Social_media =['微博','短视频','Twtter','Facebook']

def target_fliter(title,content,source):
    # print(1)
    title = cc.convert(str(title))
    content = cc.convert(str(content))

    if source in Social_media:
        label = Social_media_fliter(content)
    else:
        label = New_media_fliter(title,content)
    return label

def Social_media_fliter(content):
    label = 0
    target = 0
    text = content
    seg_dict = dict.fromkeys(targets, 0)
    for item in patten:
        obj = re.findall(item, text)
        if len(obj)>2:
            label = 1
            break
    if label == 0:
        flag = max(len(text) / 200, 1)
        word_list = list(jieba.cut(text))
        for item in word_list:
            item = item.upper()
            if len(item) > 1 and item in seg_dict.keys():
                seg_dict[item] += 1
                target += 1
                if seg_dict[item] >= flag or target > flag * 2:
                    label = 0
                    break
    return label

def New_media_fliter(title,content):
    label = 1
    target = 0
    seg_dict = dict.fromkeys(targets, 0)
    word_list = list(jieba.cut(title))
    for item in word_list:
        item = item.upper()
        if len(item) > 1 and item in targets:
            label = 0
            break
    if label == 1:
        text = title + content
        flag = max(len(text) / 400, 2)
        text_list = list(jieba.cut(text))
        for item in text_list:
            item = item.upper()
            if len(item) > 1 and item in seg_dict.keys():
                seg_dict[item] += 1
                target += 1
                if seg_dict[item] >= flag or target > flag * 2:
                    label = 0
                    break
    return label

