from .Auth import Auth
from typing import Optional, Dict, Any, Union, List


class DouYin(Auth):
    """抖音API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    # ===== 视频相关接口 =====
    def aweme_detail(self, aweme_id: Optional[str] = None, share_text: Optional[str] = None, 
                     proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情 - aweme_id和share_text必填一项"""
        data = {
            "aweme_id": aweme_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_detail", data)

    def aweme_detail_v3(self, aweme_id: Optional[str] = None, share_text: Optional[str] = None,
                        proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情v3 - aweme_id和share_text必填一项"""
        data = {
            "aweme_id": aweme_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_detail_v3", data)

    def aweme_detail_v4(self, aweme_id: Optional[str] = None, share_text: Optional[str] = None,
                        proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情v4 - aweme_id和share_text必填一项"""
        data = {
            "aweme_id": aweme_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_detail_v4", data)

    def multiple_aweme_detail(self, item_ids: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """批量获取视频详情 - item_ids格式："[xxxxxx,xxxxxx,xxxxxx]" """
        data = {
            "item_ids": item_ids,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/multiple_aweme_detail", data)

    def aweme_new_fans_count(self, aweme_id: Optional[str] = None, share_text: Optional[str] = None,
                             proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频涨粉数量 - aweme_id和share_text必填一项"""
        data = {
            "aweme_id": aweme_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_new_fans_count", data)

    # ===== 用户相关接口 =====
    def user_data(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                  proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户信息 - sec_user_id和share_text必填一项"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_data", data)

    def user_data_v2(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                     proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户信息v2 - sec_user_id和share_text必填一项"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_data_v2", data)

    def user_data_v3(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                     proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户信息v3 - sec_user_id和share_text必填一项"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_data_v3", data)

    def user_data_v4(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                     proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户信息v4 - sec_user_id和share_text必填一项"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_data_v4", data)

    def user_data_by_uid(self, uid: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """通过UID获取用户信息"""
        data = {
            "uid": uid,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_data_by_uid", data)

    def user_data_by_short(self, douyin_short: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """通过抖音号获取用户信息"""
        data = {
            "douyin_short": douyin_short,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_data_by_short", data)

    def user_tag(self, sec_user_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户标签"""
        data = {
            "sec_user_id": sec_user_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_tag", data)

    def user_post(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                  count: int = 20, max_cursor: str = "", filter_type: Optional[str] = None,
                  proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户主页发布 - sec_user_id和share_text必填一项"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "count": count,
            "max_cursor": max_cursor,
            "filter_type": filter_type,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_post", data)

    def user_post_v3(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                     count: int = 20, max_cursor: str = "",
                     proxy: Union[str, bool, None] = None, 
                     cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户最新发布 - sec_user_id和share_text必填一项"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "count": count,
            "max_cursor": max_cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/user_post_v3", data, headers)

    def user_product_data(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                          count: int = 7, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户主页作品分析数据 - sec_user_id和share_text必填一项，count为分析天数(7或30)"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "count": count,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_product_data", data)

    def user_mix(self, sec_user_id: Optional[str] = None, share_text: Optional[str] = None,
                 count: int = 20, cursor: str = "",
                 proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户合集列表 - sec_user_id和share_text必填一项"""
        data = {
            "sec_user_id": sec_user_id,
            "share_text": share_text,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_mix", data)

    def user_mix_info(self, mix_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取合集信息"""
        data = {
            "mix_id": mix_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_mix_info", data)

    def user_mix_aweme_list(self, mix_id: str, count: int = 20, cursor: str = "",
                            proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取合集视频列表"""
        data = {
            "mix_id": mix_id,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_mix_aweme_list", data)

    def search_user_aweme(self, sec_user_id: str, keyword: str, count: int = 20,
                          cursor: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索用户指定作品"""
        data = {
            "sec_user_id": sec_user_id,
            "keyword": keyword,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/search_user_aweme", data)

    def user_favorite(self, sec_user_id: str, count: int = 20, max_cursor: str = "",
                      proxy: Union[str, bool, None] = None,
                      cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户喜欢的作品"""
        data = {
            "sec_user_id": sec_user_id,
            "count": count,
            "max_cursor": max_cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/user_favorite", data, headers)

    def user_series_list(self, sec_user_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户短剧集"""
        data = {
            "sec_user_id": sec_user_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_series_list", data)

    # ===== 短剧相关接口 =====
    def series_detail(self, series_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取短剧详细信息"""
        data = {
            "series_id": series_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/series_detail", data)

    def series_aweme_list(self, series_id: str, count: int = 20, cursor: str = "",
                          proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取短剧视频列表"""
        data = {
            "series_id": series_id,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/series_aweme_list", data)

    # ===== 搜索相关接口 =====
    def general_search(self, keyword: str, count: int = 12, offset: str = "",
                       publish_time: str = "0", content_type: str = "0",
                       filter_duration: str = "0", sort_type: str = "0",
                       proxy: Union[str, bool, None] = None,
                       cookie: Optional[str] = None) -> Dict[str, Any]:
        """综合搜索"""
        data = {
            "keyword": keyword,
            "count": count,
            "offset": offset,
            "publish_time": publish_time,
            "content_type": content_type,
            "filter_duration": filter_duration,
            "sort_type": sort_type,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/general_search", data, headers)

    def general_search_v2(self, keyword: str, count: int = 12, offset: str = "",
                          publish_time: str = "0", content_type: str = "0",
                          filter_duration: str = "0", sort_type: str = "0",
                          search_id: str = "", proxy: Union[str, bool, None] = None,
                          cookie: Optional[str] = None) -> Dict[str, Any]:
        """综合搜索v2"""
        data = {
            "keyword": keyword,
            "count": count,
            "offset": offset,
            "publish_time": publish_time,
            "content_type": content_type,
            "filter_duration": filter_duration,
            "sort_type": sort_type,
            "search_id": search_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/general_search_v2", data, headers)

    def search_video(self, keyword: str, count: int = 12, offset: str = "",
                     publish_time: str = "0", filter_duration: str = "0",
                     sort_type: str = "0", search_id: str = "",
                     proxy: Union[str, bool, None] = None,
                     cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索视频"""
        data = {
            "keyword": keyword,
            "count": count,
            "offset": offset,
            "publish_time": publish_time,
            "filter_duration": filter_duration,
            "sort_type": sort_type,
            "search_id": search_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/search_video", data, headers)

    def search_video_v2(self, keyword: str, count: int = 12, offset: str = "",
                        publish_time: str = "0", filter_duration: str = "0",
                        sort_type: str = "0", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索视频v2"""
        data = {
            "keyword": keyword,
            "count": count,
            "offset": offset,
            "publish_time": publish_time,
            "filter_duration": filter_duration,
            "sort_type": sort_type,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/search_video_v2", data)

    def search_user(self, keyword: str, cursor: str = "",
                    proxy: Union[str, bool, None] = None,
                    cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索用户"""
        data = {
            "keyword": keyword,
            "cursor": cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/search_user", data, headers)

    def search_user_v2(self, keyword: str, count: int = 12, offset: str = "",
                       search_id: str = "", proxy: Union[str, bool, None] = None,
                       cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索用户v2"""
        data = {
            "keyword": keyword,
            "count": count,
            "offset": offset,
            "search_id": search_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/search_user_v2", data, headers)

    def search_music(self, keyword: str, count: int = 12, cursor: str = "",
                     search_id: str = "", proxy: Union[str, bool, None] = None,
                     cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索音乐"""
        data = {
            "keyword": keyword,
            "count": count,
            "cursor": cursor,
            "search_id": search_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/search_music", data, headers)

    def search_topic(self, keyword: str, count: int = 12, cursor: str = "",
                     search_id: str = "", proxy: Union[str, bool, None] = None,
                     cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索话题"""
        data = {
            "keyword": keyword,
            "count": count,
            "cursor": cursor,
            "search_id": search_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/douyin/search_topic", data, headers)

    def search_topic_v2(self, keyword: str, count: int = 12, cursor: str = "",
                        proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索话题v2"""
        data = {
            "keyword": keyword,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/search_topic_v2", data)

    def search_live(self, keyword: str, count: int = 15, cursor: str = "",
                    proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索直播用户"""
        data = {
            "keyword": keyword,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/search_live", data)

    def search_sug(self, keyword: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索长尾关键词"""
        data = {
            "keyword": keyword,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/search_sug", data)

    # ===== 音乐相关接口 =====
    def music_detail(self, music_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取音乐详情"""
        data = {
            "music_id": music_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/music_detail", data)

    def music_aweme(self, music_id: str, count: int = 10, cursor: str = "",
                    proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取音乐相关视频"""
        data = {
            "music_id": music_id,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/music_aweme", data)

    # ===== 话题相关接口 =====
    def challenge_detail(self, ch_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取话题详情"""
        data = {
            "ch_id": ch_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/challenge_detail", data)

    def topic_data(self, ch_id: str, count: int = 20, cursor: str = "",
                   proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取话题视频"""
        data = {
            "ch_id": ch_id,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/topic_data", data)

    def topic_data_v2(self, ch_id: str, count: int = 20, cursor: str = "",
                      proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取话题视频v2"""
        data = {
            "ch_id": ch_id,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/topic_data_v2", data)

    # ===== 评论相关接口 =====
    def video_comment(self, aweme_id: str, count: int = 20, cursor: str = "",
                      proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频一级评论"""
        data = {
            "aweme_id": aweme_id,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/video_comment", data)

    def video_sub_comment(self, aweme_id: str, comment_id: str, count: int = 20, cursor: str = "",
                          proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频二级评论"""
        data = {
            "aweme_id": aweme_id,
            "comment_id": comment_id,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/video_sub_comment", data)

    # ===== 直播相关接口 =====
    def live_room_data(self, web_rid: Optional[str] = None, share_text: Optional[str] = None,
                       proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """通过web_rid获取直播间信息 - web_rid和share_text必填一项"""
        data = {
            "web_rid": web_rid,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/live_room_data", data)

    def live_room_by_id(self, room_id: Optional[str] = None, share_text: Optional[str] = None,
                        proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """通过ID获取直播间信息 - room_id和share_text必填一项"""
        data = {
            "room_id": room_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/live_room_by_id", data)

    def check_user_live_status(self, sec_user_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """检查用户直播状态"""
        data = {
            "sec_user_id": sec_user_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/check_user_live_status", data)

    def live_user_data(self, web_rid: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取开放直播间用户列表"""
        data = {
            "web_rid": web_rid,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/live_user_data", data)

    def live_room_by_map(self, latitude: str, longitude: str, distance: str = "10000",
                         cursor: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取同城直播"""
        data = {
            "latitude": latitude,
            "longitude": longitude,
            "distance": distance,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/live_room_by_map", data)

    # ===== 弹幕相关接口 =====
    def aweme_danmaku(self, aweme_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频弹幕"""
        data = {
            "aweme_id": aweme_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_danmaku", data)

    # ===== 短链相关接口 =====
    def user_short_link(self, sec_user_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户主页短连接"""
        data = {
            "sec_user_id": sec_user_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/user_short_link", data)

    def aweme_short_link(self, aweme_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频短连接"""
        data = {
            "aweme_id": aweme_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_short_link", data)

    def aweme_qr_code(self, aweme_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """生成视频抖音码"""
        data = {
            "aweme_id": aweme_id,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_qr_code", data)

    def aweme_shorten(self, aweme_id: str, aweme_type: str = "video",
                      proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取分享短链"""
        data = {
            "aweme_id": aweme_id,
            "aweme_type": aweme_type,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_shorten", data)

    # ===== 热点相关接口 =====
    def hot_spot_aladdin(self, words: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """热点讨论"""
        data = {
            "words": words,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/hot_spot_aladdin", data)

    def aweme_board(self, board_type: str = "1", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """抖音热榜"""
        data = {
            "board_type": board_type,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/aweme_board", data)

    # ===== 其他功能接口 =====
    def share_to_scheme(self, url: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取协议链接"""
        data = {
            "url": url,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/share_to_scheme", data)

    def near_by(self, latitude: str, longitude: str, count: int = 20, cursor: str = "",
                proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取同城视频"""
        data = {
            "latitude": latitude,
            "longitude": longitude,
            "count": count,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/near_by", data)

    def medium_channel_feed(self, channel_id: str, cursor: str = "",
                            proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取抖音精选"""
        data = {
            "channel_id": channel_id,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/douyin/medium_channel_feed", data) 