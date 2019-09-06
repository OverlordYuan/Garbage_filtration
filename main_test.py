# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
from Spam_Text_Recognition_local import Spam

if __name__ =='__main__':
    a = Spam('华为')
    data_pd = a.read_csv()
    # type = list(set(data_pd['source'].tolist()))
    # print(type)
    # data_pd = a.read_xls()
    # type = list(set(data_pd['source'].tolist()))
    # print(type)
    # data_pd.to_csv('input/华为/huawei.csv')
    d = a.Garbage_analysis(data_pd)
    # print(data_pd.shape)
    a.save_rusult(d)
