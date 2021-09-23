# -*- coding:utf-8 -*-

import time
import random
import requests
import pandas as pd

print('---开始爬取---')
# UA伪装
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
}
print('---UA伪装完成---')
# 指定URL
url = 'https://movie.douban.com/j/chart/top_list?'
print('---指定URL完成---')

movie_type = {
    '剧情':'11', '喜剧':'24','动作':'5', '爱情':'13','科幻':'17','动画':'25','悬疑':'10','惊悚':'19','纪录片':'1',
'短片':'23','恐怖':'20','情色':'6','同性':'26','音乐':'14','歌舞':'7','家庭':'28','儿童':'8','传记':'2','历史':'4',
'战争':'22','犯罪':'3','西部':'27','奇幻':'16','冒险':'15','灾难':'12','武侠':'29','古装':'30','运动':'18','黑色电影':'31',
}

for key in movie_type.keys():
    print('开始爬取{0}类型Top100'.format(key))
    movie_top100 = pd.DataFrame(columns=['评分','片名','年份','地区','豆瓣链接'])
    # 指定请求参数
    param = {
       'type': movie_type[key], # 指定分类类型
        'interval_id': '100:90',
        'action': '',
        'start': '0', # 指定从哪里开始
        'limit': '100' # 指定需要爬取多少部
    }
    print('---指定请求参数完成---')
    print('---正在发送请求---')
    # 发送请求
    response = requests.get(url=url, params=param, headers=header)
    # 获取响应数据
    dic_list = response.json()
    print('---已获取响应数据---')
    for i in range(len(dic_list)):
        lst = []
        lst.append(dic_list[i]['rating'][0])
        lst.append(dic_list[i]['title'])
        lst.append(dic_list[i]['release_date'])
        lst.append(dic_list[i]['regions'])
        lst.append(dic_list[i]['url'])
        movie_top100.loc[i] = lst
    # 保存数据
    movie_top100.to_csv('豆瓣电影排行榜TOP100-{0}.csv'.format(key), )
    print('---{0}类型保存完成---'.format(key))
    print('————下一个类型————')
    time.sleep(random.randint(5,10))

print('全部完成！')


