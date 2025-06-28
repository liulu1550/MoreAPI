from .Auth import Auth
from typing import Optional, Dict, Any, Union, List


class KuaiShou(Auth):
    """快手API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    # ===== 视频相关接口 =====
    def aweme_detail(self, share_text: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情"""
        data = {
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/ks/aweme_detail", data)

    def aweme_detail_app(self, photo_id: Union[str, List[str]], proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情v3"""
        data = {
            "photo_id": photo_id,
            "proxy": proxy
        }
        return self._make_request("/api/ks/aweme_detail_app", data)

    def video_comment(self, aweme_id: str, pcursor: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频评论"""
        data = {
            "aweme_id": aweme_id,
            "pcursor": pcursor,
            "proxy": proxy
        }
        return self._make_request("/api/ks/video_comment", data)

    # ===== 用户相关接口 =====
    def user_post(self, user_id: str, pcursor: str = "", proxy: Union[str, bool, None] = None,
                  cookie: str = "") -> Dict[str, Any]:
        """获取用户主页发布"""
        data = {
            "user_id": user_id,
            "pcursor": pcursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/ks/user_post", data, headers)

    def user_post_v3(self, user_id: str, pcursor: str = "", proxy: Union[str, bool, None] = None,
                     cookie: str = "") -> Dict[str, Any]:
        """获取用户主页发布v3"""
        data = {
            "user_id": user_id,
            "pcursor": pcursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/ks/user_post_v3", data, headers)

    def user_data(self, user_id: str, proxy: Union[str, bool, None] = None,
                  cookie: str = "") -> Dict[str, Any]:
        """获取用户详情"""
        data = {
            "user_id": user_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/ks/user_data", data, headers)

    def user_data_v2(self, user_id: str, proxy: Union[str, bool, None] = None,
                     cookie: str = "") -> Dict[str, Any]:
        """获取用户详情v2"""
        data = {
            "user_id": user_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/ks/user_data_v2", data, headers)

    # ===== 搜索相关接口 =====
    def search_aweme(self, query: str, pcursor: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索视频"""
        data = {
            "query": query,
            "pcursor": pcursor,
            "proxy": proxy
        }
        return self._make_request("/api/ks/search_aweme", data)

    # ===== 其他功能接口 =====
    def aweme_share_link(self, aweme_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频分享链接"""
        data = {
            "aweme_id": aweme_id,
            "proxy": proxy
        }
        return self._make_request("/api/ks/aweme_share_link", data) 