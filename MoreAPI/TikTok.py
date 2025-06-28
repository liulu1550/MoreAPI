from .Auth import Auth
from typing import Optional, Dict, Any, Union


class TikTok(Auth):
    """TikTok API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    # ===== 视频相关接口 =====
    def aweme_detail(self, aweme_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情"""
        data = {
            "aweme_id": aweme_id,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/aweme_detail", data)

    # ===== 用户相关接口 =====
    def user_data(self, sec_uid: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户详情"""
        data = {
            "sec_uid": sec_uid,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/user_data", data)

    def user_post(self, sec_uid: str, count: int = 10, max_cursor: str = "",
                  proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户主页发布"""
        data = {
            "sec_uid": sec_uid,
            "count": count,
            "max_cursor": max_cursor,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/user_post", data)

    # ===== 评论相关接口 =====
    def video_comment(self, aweme_id: str, cursor: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取作品父评论"""
        data = {
            "aweme_id": aweme_id,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/video_comment", data)

    def video_sub_comment(self, aweme_id: str, comment_id: str, cursor: str = "",
                          proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取作品子评论"""
        data = {
            "aweme_id": aweme_id,
            "comment_id": comment_id,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/video_sub_comment", data)

    # ===== 搜索相关接口 =====
    def general_search(self, keyword: str, offset: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """综合搜索"""
        data = {
            "keyword": keyword,
            "offset": offset,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/general_search", data)

    def search_user(self, keyword: str, offset: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索用户"""
        data = {
            "keyword": keyword,
            "offset": offset,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/search_user", data)

    def search_item(self, keyword: str, offset: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索视频"""
        data = {
            "keyword": keyword,
            "offset": offset,
            "proxy": proxy
        }
        return self._make_request("/api/tiktok/search_item", data) 