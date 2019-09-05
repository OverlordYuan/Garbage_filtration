# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import Pattern_filtering as pf

def Judgment_function(title,content,source,target):
    label = 0
    label = pf.filter(title, content,label)
    try:
        if source == '微博' or len(str(content)) < 200:
            label = pf.filter(title, content)
        else:
            label = pf.target_fliter(title,content,target)
    except:
        pass
    return str(label)