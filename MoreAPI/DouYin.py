import requests

import MoreAPI
from MoreAPI.Auth import Auth
from MoreAPI.http_fetch import post_request


class DouYin(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.video_data_url = self.domain + "/api/douyin/aweme_detail"
        self.user_data_url = self.domain + "/api/douyin/user_data"
        self.user_video_data_url = self.domain + "/api/douyin/user_post"
        self.user_mix_url = self.domain + "/api/douyin/user_mix"
        self.user_mix_aweme_list_url = self.domain + "/api/douyin/user_mix_aweme_list"
        self.search_user_aweme_url = self.domain + "/api/douyin/search_user_aweme"
        self.user_favorite_url = self.domain + "/api/douyin/user_favorite"
        self.video_comment_url = self.domain + "/api/douyin/video_comment"
        self.video_sub_comment_url = self.domain + "/api/douyin/video_sub_comment"
        self.general_search_url = self.domain + "/api/douyin/general_search"
        self.search_video_url = self.domain + "/api/douyin/search_video"
        self.search_video_url = self.domain + "/api/douyin/search_video_v2"
        self.search_user_url = self.domain + "/api/douyin/search_user_v3"
        self.search_music_url = self.domain + "/api/douyin/search_music"
        self.music_detail_url = self.domain + "/api/douyin/music_detail"
        self.music_aweme_url = self.domain + "/api/douyin/music_aweme"
        self.search_live_url = self.domain + "/api/douyin/search_live"
        self.live_room_data_url = self.domain + "/api/douyin/live_room_data"
        self.search_topic_url = self.domain + "/api/douyin/search_topic"
        self.challenge_detail_url = self.domain + "/api/douyin/challenge_detail"
        self.topic_data_url = self.domain + "/api/douyin/topic_data"
        self.aweme_danmaku_url = self.domain + "/api/douyin/aweme_danmaku"
        self.aweme_short_link_url = self.domain + "/api/douyin/aweme_short_link"
        self.aweme_qr_code_url = self.domain + "/api/douyin/aweme_qr_code"
        self.search_sug_url = self.domain + "/api/douyin/search_sug"
        self.hot_spot_aladdin_url = self.domain + "/api/douyin/hot_spot_aladdin"

    def aweme_detail(self, aweme_id: str = None, share_text: str = None) -> dict:
        _json_data = {
            "aweme_id": aweme_id,
            "share_text": share_text
        }
        return post_request(url=self.video_data_url, json_data=_json_data, headers=self.headers)

    def user_data(self, sec_user_id: str = None, share_text: str = None) -> dict:
        _json_data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text
        }
        return post_request(url=self.user_data_url, json_data=_json_data, headers=self.headers)

    def user_post(self, sec_user_id: str = None, share_text: str = None, max_cursor: str = None, count: str = "20",
                  filter_type: str = None) -> dict:
        _json_data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "max_cursor": max_cursor,
            "count": count,
            "filter_type": filter_type
        }
        return post_request(url=self.user_video_data_url, json_data=_json_data, headers=self.headers)

    def user_mix(self, sec_user_id: str = None, share_text: str = None, cursor: str = '0', count: str = "10") -> dict:
        _json_data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "cursor": cursor,
            "count": count
        }
        return post_request(url=self.user_mix_url, json_data=_json_data, headers=self.headers)

    def user_mix_aweme_list(self, mix_id: str = None, cursor: str = '0', count: str = "10") -> dict:
        _json_data = {
            "mix_id": mix_id,
            "cursor": cursor,
            "count": count
        }
        return post_request(url=self.user_mix_aweme_list_url, json_data=_json_data, headers=self.headers)

    def search_user_aweme(self, uid: str = None, keyword: str = None, cursor: str = '0', count: str = "10") -> dict:
        _json_data = {
            "uid": uid,
            "keyword": keyword,
            "cursor": cursor,
            "count": count
        }
        return post_request(url=self.search_user_aweme_url, json_data=_json_data, headers=self.headers)

    def user_favorite(self, sec_user_id: str = None, share_text: str = None, cursor: str = '0',
                      count: str = "10") -> dict:
        _json_data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "cursor": cursor,
            "count": count
        }
        return post_request(url=self.user_favorite_url, json_data=_json_data, headers=self.headers)

    def video_comment(self, aweme_id: str = None, share_text: str = None, cursor: str = '0',
                      count: str = "20") -> dict:
        _json_data = {
            "aweme_id": aweme_id,
            "share_text": share_text,
            "cursor": cursor,
            "count": count
        }
        return post_request(url=self.video_comment_url, json_data=_json_data, headers=self.headers)

    def video_sub_comment(self, aweme_id: str = None, comment_id: str = None, cursor: str = '0',
                          count: str = "20") -> dict:
        _json_data = {
            "aweme_id": aweme_id,
            "comment_id": comment_id,
            "cursor": cursor,
            "count": count
        }
        return post_request(url=self.video_sub_comment_url, json_data=_json_data, headers=self.headers)

    def general_search(self, keyword: str = None, sort_type: str = "", publish_time: str = '', offset: str = '0',
                       count: str = "20") -> dict:
        _json_data = {
            "keyword": keyword,
            "sort_type": sort_type,
            "publish_time": publish_time,
            "offset": offset,
            "count": count
        }
        return post_request(url=self.general_search_url, json_data=_json_data, headers=self.headers)
