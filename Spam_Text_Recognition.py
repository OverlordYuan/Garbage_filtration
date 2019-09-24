# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import re,pickle
import jieba
import opencc
# import fool
from patten_config import patten

jieba.load_userdict("cut_dict.txt")
cc = opencc.OpenCC('t2s')
with open('targets.txt', 'rb') as f:
    targets = pickle.load(f)

Social_media =['微博','短视频','Twtter','Facebook']
def target_fliter(title,content,source):
    # print(1)
    label = 1
    target = 0
    title = cc.convert(str(title))
    content = cc.convert(str(content))
    seg_dict = dict.fromkeys(targets, 0)
    text = title + content
    word_list =list(jieba.cut(title))
    # print(word_list)
    if source not in Social_media:
        for item in word_list:
            item = item.upper()
            if len(item)>1 and item in targets:
                # print(2)
                label = 0
                break
    if label==1:
        if source in Social_media:
            flag = 3
            for item in patten:
                text = re.compile(item).sub('',text)
        else:
            flag = max(len(text) / 400, 2)

        text_list = list(jieba.cut(text))
        # print(text_list)
        for item in text_list:
            item = item.upper()
            if len(item)>1 and item in seg_dict.keys():
                seg_dict[item] += 1
                target += 1
                if seg_dict[item]>=flag or target>flag*2:
                    label = 0
                    break
    return label


