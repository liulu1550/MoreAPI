#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : MoreAPI
@File    : Bilibili.py
@Author  : MoreCoding多点部落
@Time    : 2023/9/14 11:43 AM
"""
import requests

from MoreAPI.Auth import Auth


class Bilibili(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.video_data_url = self.domain + "/api/bilibili/video_data"
        self.video_download_url = self.domain + "/api/bilibili/video_download"
        self.user_post_url = self.domain + "/api/bilibili/user_post"
        self.search_data_url = self.domain + "/api/bilibili/search"

    def video_data(self, bvid: str):
        """
        获取视频信息
        :param bvid: BV 号
        :return:
        """
        if not bvid:
            return None
        try:
            result = requests.get(self.video_data_url, headers=self.headers, params={"bvid": bvid})
        except:
            return None

        return result.json()

    def user_post(self, user_id: str):
        """
        获取视频信息
        :param user_id: 用户ID
        :return:
        """
        if not user_id:
            return None
        try:
            result = requests.get(self.user_post_url, headers=self.headers, params={"user_id": user_id})
        except:
            return None

        return result.json()

    def video_download(self, bvid: str, cookie: str = None):
        """
        获取视频下载链接
        :param bvid: BV 号
        :param cookie: 个人cookie
        :return:
        """
        if not bvid:
            return None
        try:
            result = requests.get(self.video_download_url, headers=self.headers, cookies=cookie, params={"bvid": bvid})
        except:
            return None

        return result.json()

    def search_data(self, keyword: str, search_type: str = None, order_type: str = None, order_sort: str = None,
                    page: str = None):
        """
        搜索数据
        :param keyword: 关键词
        :param search_type: VIDEO:视频，BANGUMI:番剧，FT:影视, LIVE : 直播, ARTICLE : 专栏, TOPIC : 话题, USER : 用户, LIVEUSER : 直播间用户  (默认为VIDEO)
        :param order_type: 排序分类类型：search_type为VIDEO时：TOTALRANK：综合，CLICK：最多点击，PUBDATE：最新发布，DM：最多弹幕, STOW : 最多收藏， SCORES : 最多评论。
                                        search_type为USER时：FANS : 按照粉丝数量排序， LEVEL : 按照等级排序。
                                        search_type为LIVE时：NEWLIVE 最新开播， ONLINE 综合排序。
                                        search_type为ARTICLE时：TOTALRANK : 综合排序， CLICK : 最多点击， PUBDATE : 最新发布， ATTENTION : 最多喜欢， SCORES : 最多评论
        :param order_sort: 由高到低：0 由低到高：1
        :param page: 页码
        :return:
        """
        if not keyword:
            return None
        try:
            result = requests.get(self.search_data_url, headers=self.headers,
                                  params={"keyword": keyword, "search_type": search_type, "order_type": order_type,
                                          "order_sort": order_sort, "page": page})
        except:
            return None

        return result.json()
