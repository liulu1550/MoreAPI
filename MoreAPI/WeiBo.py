#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : MoreAPI
@File    : WeiBo.py
@Author  : MoreCoding多点部落
@Time    : 2023/10/17 9:27 AM
"""
import requests

from MoreAPI.Auth import Auth


class WeiBo(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.get_user_info_url = self.domain + "/api/weibo/user_info"
        self.get_user_post_url = self.domain + "/api/weibo/user_post"
        self.get_hot_search_url = self.domain + "/api/weibo/hot_search"
        self.get_note_comments_url = self.domain + "/api/weibo/comments"
        self.get_note_sub_comments_url = self.domain + "/api/weibo/sub_comments"

    def get_user_info(self, uid=str):
        """
        获取用户信息
        :param uid: 用户UID(例：https://weibo.com/u/2656274875，2656274875就是用户UID)
        :return:
        """
        if not uid:
            return None
        try:
            result = requests.get(self.get_user_info_url, headers=self.headers, params={"uid": uid})
        except:
            return None
        return result.json()

    def get_user_post(self, uid: str, page: int = 1):
        """
        获取用户发布
        :param uid: 用户UID(例：https://weibo.com/u/2656274875，2656274875就是用户UID)
        :param page: 页码
        :return:
        """
        if not uid:
            return None
        try:
            result = requests.get(self.get_user_post_url, headers=self.headers, params={"uid": uid, "page": page})
        except:
            return None
        return result.json()

    def get_hot_search(self):
        """
        获取热搜列表
        :return:
        """
        try:
            result = requests.get(self.get_hot_search_url, headers=self.headers)
        except:
            return None
        return result.json()
