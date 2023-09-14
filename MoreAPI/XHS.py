#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : MoreAPI
@File    : XHS.py
@Author  : MoreCoding多点部落
@Time    : 2023/9/14 11:11 AM
"""
import requests

from MoreAPI.Auth import Auth


class XHS(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.get_note_by_id_url = self.domain + "/api/xhs/get_note_by_id/"
        self.get_user_info_url = self.domain + "/api/xhs/get_user_info/"
        self.get_user_notes_url = self.domain + "/api/xhs/get_user_notes/"
        self.get_note_comments_url = self.domain + "/api/xhs/get_note_comments/"
        self.get_note_sub_comments_url = self.domain + "/api/xhs/get_note_sub_comments/"
        self.search_note_by_keyword_url = self.domain + "/api/xhs/search_note_by_keyword/"

    def get_note_by_id(self, note_id: str, cookie: str = None):
        """
        获取笔记详情
        :param note_id: 笔记ID
        :param cookie: 个人cookie
        :return:
        """
        if not note_id:
            return None
        try:
            result = requests.get(self.get_note_by_id_url, headers=self.headers, cookies=cookie,
                                  params={"note_id": note_id})
        except:
            return None
        return result.json()

    def get_user_info(self, user_id: str, cookie: str = None):
        """
        获取个人信息
        :param user_id: 作者ID
        :param cookie:个人cookie
        :return:
        """
        if not user_id:
            return None
        try:
            result = requests.get(self.get_user_info_url, headers=self.headers, cookies=cookie,
                                  params={"user_id": user_id})
        except:
            return None
        return result.json()

    def get_user_note(self, user_id: str, cursor: str = None, type: str = None, cookie: str = None):
        """
        获取用户笔记
        :param user_id: 作者ID
        :param cursor: 下一页参数
        :param type: 类型。默认为空获取用户发布的笔记。（collect:获取用户收藏笔记，like:获取用户点赞笔记）
        :param cookie: 个人cookie
        :return:
        """
        if not user_id:
            return None
        try:
            result = requests.get(self.get_user_notes_url, headers=self.headers, cookies=cookie,
                                  params={"user_id": user_id, "cursor": cursor, "type": type})
        except:
            return None
        return result.json()

    def get_note_comments(self, note_id: str, cursor: str = None, cookie: str = None):
        """
        获取笔记评论
        :param note_id: 笔记ID
        :param cursor: 页码参数
        :param cookie: 个人cookie
        :return:
        """
        if not note_id:
            return None
        try:
            result = requests.get(self.get_note_comments_url, headers=self.headers, cookies=cookie,
                                  params={"note_id": note_id, "cursor": cursor})
        except:
            return None
        return result.json()

    def get_note_sub_comments(self, note_id: str, root_comment_id: str, cursor: str = None, num: str = "10",
                              cookie: str = None):
        """
        获取笔记下评论的子评论
        :param note_id: 笔记ID
        :param root_comment_id: 父评论ID
        :param cursor: 页码参数
        :param num: 当前页条数（默认10）
        :param cookie: 个人cookie
        :return:
        """

        if not note_id or not note_id:
            return None
        try:
            result = requests.get(self.get_note_sub_comments_url, headers=self.headers, cookies=cookie,
                                  params={"note_id": note_id, "root_comment_id": root_comment_id, "cursor": cursor,
                                          "num": num})
        except:
            return None
        return result.json()

    def search_note_by_keyword(self, keyword: str, page: int = 1, page_size: int = 20, sort: str = "general",
                               note_type: str = "video", cookie: str = None):
        """
        搜索笔记
        :param keyword: 关键词
        :param page: 页码（默认1）
        :param page_size: 每页条数（默认20）
        :param sort: 排序方式。general:默认, hot:最热, new:最新
        :param note_type: 搜索结果类型（默认all）。all:全部,video:视频, image:图集
        :param cookie: 个人cookie
        :return:
        """
        if not keyword:
            return None
        try:
            result = requests.get(self.search_note_by_keyword_url, headers=self.headers, cookies=cookie,
                                  params={"keyword": keyword, "page": page, "page_size": page_size,
                                          "sort": sort, "note_type": note_type})
        except:
            return None
        return result.json()
