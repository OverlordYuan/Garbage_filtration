# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import Spam_Text_Recognition as st

def Judgment_function(title,content,source,target):
    label = 0
    label = st.filter(title, content,label)
    try:
        if source == '微博' or len(str(content)) < 200:
            label = st.filter(title, content)
        else:
            label = st.target_fliter(title,content,target)
    except:
        pass
    return str(label)