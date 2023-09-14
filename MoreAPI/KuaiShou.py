#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : MoreAPI
@File    : KuaiShou.py
@Author  : MoreCoding多点部落
@Time    : 2023/9/14 10:55 AM
"""
import requests

from MoreAPI.Auth import Auth


class KuaiShou(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.user_video_data_url = self.domain + "/api/ks/user_video_data/"
        self.video_data_url = self.domain + "/api/ks/video_data/"
        self.user_data_url = self.domain + "/api/ks/user_data/"
        self.comments_list_url = self.domain + "/api/ks/comments_list/"
        self.sub_comments_list_url = self.domain + "/api/ks/sub_comments_list/"
        self.search_data_url = self.domain + "/api/ks/search/"

    def user_video_data(self, user_id: str, cursor: str = None, cookie: str = None):
        """
        获取用户主页视频数据
        :param user_id: 用户ID
        :param cursor: 下一页参数
        :param cookie: 个人cookie
        :return:
        """
        if not user_id:
            return None

        try:
            result = requests.get(self.user_video_data_url, headers=self.headers, cookies=cookie,
                                  params={"user_id": user_id, "cursor": cursor})
        except:
            return None

        return result.json()

    def video_data(self, video_id: str, cookie: str = None):
        """
        获取视频详情
        :param video_id: 视频ID
        :param cookie: 个人cookie
        :return:
        """
        if not video_id:
            return None

        try:
            result = requests.get(self.video_data_url, headers=self.headers, cookies=cookie,
                                  params={"video_id": video_id})
        except:
            return None

        return result.json()

    def user_data(self, user_id: str, cookie: str = None):
        """
        获取用户信息
        :param user_id:  用户ID
        :param cookie: 个人cookie
        :return:
        """
        if not user_id:
            return None

        try:
            result = requests.get(self.user_data_url, headers=self.headers, cookies=cookie,
                                  params={"user_id": user_id})
        except:
            return None

        return result.json()

    def comments_list(self, video_id: str, pcursor: str = None, cookie: str = None):
        """
        获取视频评论列表
        :param video_id:  视频ID
        :param pcursor:  下一页参数
        :param cookie: 个人cookie
        :return:
        """
        if not video_id:
            return None

        try:
            result = requests.get(self.comments_list_url, headers=self.headers, cookies=cookie,
                                  params={"video_id": video_id, "pcursor": pcursor})
        except:
            return None

        return result.json()

    def sub_comments_list(self, video_id: str, root_id: str, pcursor: str = None, cookie: str = None):
        """
        获取子评论列表
        :param video_id: 视频ID
        :param root_id: 父评论ID
        :param pcursor: 下一页参数
        :param cookie: 个人cookie
        :return:
        """
        if not video_id or not root_id:
            return None

        try:
            result = requests.get(self.comments_list_url, headers=self.headers, cookies=cookie,
                                  params={"video_id": video_id, "pcursor": pcursor, "root_id": root_id})
        except:
            return None

        return result.json()

    def search_data(self, keyword: str, type: str = "video", pcursor: str = None, cookie: str = None):
        """
        搜索数据
        :param keyword: 关键词
        :param type: video/user,搜索视频和用户
        :param pcursor: 页数
        :param cookie: 个人cookie
        :return:
        """
        if not keyword:
            return None

        try:
            result = requests.get(self.search_data_url, headers=self.headers, cookies=cookie,
                                  params={"keyword": keyword, "type": type, "pcursor": pcursor})
        except:
            return None

        return result.json()
