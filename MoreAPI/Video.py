#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : MoreAPI
@File    : Video.py
@Author  : MoreCoding多点部落
@Time    : 2023/9/14 1:54 PM
"""
import requests

from MoreAPI.Auth import Auth


class Video(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.video_data_url = self.domain + "/api/video/"

    def video_data(self, share_text: str):
        """
        获取视频详情
        :param share_text: 视频ID
        :return:
        """

        if not share_text:
            return None
        try:
            result = requests.get(self.video_data_url, headers=self.headers, params={"share_text": share_text})
        except:
            return None
        return result.json()
