#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：MoreAPI 
@File    ：ttt.py
@IDE     ：PyCharm 
@Author  ：多点部落  https://www.wouldmissyou.com
@Date    ：2024/7/3 14:37 
@WebSite ：https://www.wouldmissyou.com
'''
import time

import requests

url = "http://moreapi.99anji.com/api/douyin/user_post"

params={
    "sec_user_id":"MS4wLjABAAAAnAGN9Xjl_X2_PJsVeERo6mYg8DKIsjwXMfaEog5Tspg",
    "share_text":"",
    "max_cursor":"",
    "count":"50",
    "filter_type":""
}

t1 = time.time()
response = requests.request("POST", url, json=params)
t2 = time.time()

print(response.text)
print(f"消耗：{t2-t1}")