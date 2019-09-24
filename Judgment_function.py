# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import Spam_Text_Recognition  as st

def Judgment_function(title,content,source):
    label = 1
    try:
        # print(1)
        label = st.target_fliter(title,content,source)
    except Exception as e:
        # print(0)
        print(e)
    return str(label)