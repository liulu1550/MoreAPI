#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : MoreAPI
@File    : YouTube.py
@Author  : MoreCoding多点部落
@Time    : 2023/9/14 1:47 PM
"""
import requests

from MoreAPI.Auth import Auth


class YouTube(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.video_data_url = self.domain + "/api/youtube/video_data"
        self.video_comments_url = self.domain + "/api/youtube/video_comments"
        self.search_data_url = self.domain + "/api/youtube/search"

    def video_data(self, video_id: str):
        """
        获取视频详情
        :param video_id: 视频ID
        :return:
        """

        if not video_id:
            return None
        try:
            result = requests.get(self.video_data_url, headers=self.headers, params={"video_id": video_id})
        except:
            return None
        return result.json()

    def video_comments(self, video_id: str, max_results: int = 40, order: str = "time", page_token: str = None):
        """
        获取视频评论
        :param video_id: 视频ID
        :param max_results: 每页条数
        :param order: 排序方式（time:按时间排序， relevance：按热门排序）
        :param page_token: 下一页参数
        :return:
        """
        if not video_id:
            return None
        try:
            result = requests.get(self.video_data_url, headers=self.headers,
                                  params={"video_id": video_id, "max_results": max_results, "order": order,
                                          "page_token": page_token})
        except:
            return None
        return result.json()

    def search_data(self, keywords: str, max_results: int = 20, order: str = "relevance", page_token: str = None,
                    video_type: str = "any", region_code: str = "HK"):
        """
        搜索数据
        :param keywords: 关键词
        :param max_results: 每页条数
        :param order: 排序（rating:按评分从高到低排序。viewCount:按浏览次数从高到低排序。relevance:按与搜索查询的相关性排序。date:按照创建时间倒序排列。title:按标题的字母顺序排序。videoCount:频道已上传的视频数量按降序排序）
        :param page_token: 下一页参数
        :param video_type: any - 返回所有视频。episode - 仅检索节目的剧集。movie - 仅检索影片。
        :param region_code: 国家序号。US：美国,TW:中国台湾', HK:中国香港, SG:新加坡, JP:日本, IE:爱尔兰, IN:印度, FR:法国, CA:加拿大
        :return:
        """

        if not keywords:
            return None
        try:
            result = requests.get(self.search_data_url, headers=self.headers,
                                  params={"keywords": keywords, "max_results": max_results, "order": order,
                                          "page_token": page_token, "video_type": video_type,
                                          "region_code": region_code})
        except:
            return None

        return result.json()
