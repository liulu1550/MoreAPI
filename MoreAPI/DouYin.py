import requests

import MoreAPI
from MoreAPI.Auth import Auth


class DouYin(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.video_data_url = self.domain + "/api/douyin/video_data/"
        self.user_data_url = self.domain + "/api/douyin/user_data/"
        self.user_video_data_url = self.domain + "/api/douyin/user_video_data/"
        self.live_room_data_url = self.domain + "/api/douyin/live_room/"
        self.video_comment_url = self.domain + "/api/douyin/video_comment/"
        self.search_data_url = self.domain + "/api/douyin/search/"

    def aweme_data(self, aweme_id: str, cookie: str = None):
        """
        获取单一视频信息
        :param aweme_id:  视频ID
        :return:
        """
        if not aweme_id:
            return None
        try:
            result = requests.get(url=self.video_data_url, headers=self.headers, cookies=cookie,
                                  params={"aweme_id": aweme_id})
        except:
            return None

        return result.json()

    def user_data(self, sec_user_id: str, cookie: str = None):
        """
        获取用户信息
        :param sec_user_id: 用户iD
        :param cookie: 个人cookie
        :return:
        """
        if not sec_user_id:
            return None
        try:
            result = requests.get(url=self.user_data_url, headers=self.headers, cookies=cookie,
                                  params={"sec_user_id": sec_user_id})
        except:
            return None
        return result.json()

    def user_video_data(self, sec_user_id: str, count: int = 20, max_cursor: str = None, cookie: str = None):
        """
        获取用户主页视频
        :param sec_user_id: 用户ID
        :param count: 数量（默认20）
        :param max_cursor:下一页参数（默认0）
        :param cookie:个人cookie
        :return:
        """
        if not sec_user_id:
            return None
        try:
            result = requests.get(url=self.user_video_data_url, headers=self.headers, cookies=cookie,
                                  params={"sec_user_id": sec_user_id, "count": count, "max_cursor": max_cursor})
        except:
            return None
        return result.json()

    def live_room(self, web_rid: str = None, cookie: str = None):
        """
        获取直播间信息
        :param web_rid: 抖音直播间ID
        :param cookie: 个人cookie
        :return:
        """
        if not web_rid:
            return None
        try:
            result = requests.get(url=self.live_room_data_url, headers=self.headers, cookies=cookie,
                                  params={"web_rid": web_rid})
        except:
            return None
        return result.json()

    def video_comment(self, aweme_id: str, cursor: int = 0, count: int = 20, cookie: str = None):
        """
        获取作品评论
        :param aweme_id: 作品ID
        :param cursor: 下一页参数
        :param count: 每页个数
        :param cookie: 个人cookie
        :return:
        """
        if not aweme_id:
            return None
        try:
            result = requests.get(url=self.video_comment_url, headers=self.headers, cookies=cookie,
                                  params={"aweme_id": aweme_id, "cursor": cursor, "count": count})
        except:
            return None
        return result.json()

    def search_data(self, keyword: str, search_type: str = "general", sort_type: int = 0, publish_time: int = 0,
                    offset: int = 0, count: int = 10, cookie: str = None):
        """
        搜索数据
        :param keyword: 搜索关键词
        :param search_type: 搜索类型，默认general。general/综合搜索   video/视频搜索   user/搜索用户   live/搜索直播
        :param sort_type: 排序方式，默认0。 0/综合排序， 2/最新发布, 1/最多点赞。（类型为：general或video时生效）
        :param publish_time: 发布时间，默认0。 0/不限， 1/一天内, 7/一周内， 182/半年内。（类型为：general或video时生效）
        :param offset: 页码，默认0
        :param count: 每页条数，默认10
        :param cookie: 个人cookie
        :return:
        """
        if not keyword:
            return None
        try:
            result = requests.get(url=self.search_data_url, headers=self.headers, cookies=cookie,
                                  params={"keyword": keyword, "search_type": search_type, "sort_type": sort_type,
                                          "publish_time": publish_time, "offset": offset, "count": count})
        except:
            return None

        return result.json()