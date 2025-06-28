from .Auth import Auth
from typing import Optional, Dict, Any, Union


class Billboard(Auth):
    """榜单API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    def billboard_category(self, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取榜单分类"""
        data = {
            "proxy": proxy
        }
        return self._make_request("/api/billboard/billboard_category", data)

    def rise(self, billboard_type: str, cursor: str = "",
             proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取上升榜"""
        data = {
            "billboard_type": billboard_type,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/rise", data)

    def city_value(self, billboard_type: str, city_code: str,
                   proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取城市榜单数据"""
        data = {
            "billboard_type": billboard_type,
            "city_code": city_code,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/city_value", data)

    def city_billboard(self, billboard_type: str, city_code: str, cursor: str = "",
                       proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取城市榜单"""
        data = {
            "billboard_type": billboard_type,
            "city_code": city_code,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/city_billboard", data)

    def challenge_billboard(self, billboard_type: str, cursor: str = "",
                           proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取话题榜单"""
        data = {
            "billboard_type": billboard_type,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/challenge_billboard", data)

    def total_billboard(self, billboard_type: str, cursor: str = "",
                        proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取总榜单"""
        data = {
            "billboard_type": billboard_type,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/total_billboard", data)

    def billboard_video(self, billboard_type: str, cursor: str = "",
                        proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频榜单"""
        data = {
            "billboard_type": billboard_type,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/billboard_video", data)

    def user_fans_data(self, sec_user_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户粉丝数据"""
        data = {
            "sec_user_id": sec_user_id,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/user_fans_data", data)

    def user_fans_interest(self, sec_user_id: str, interest_type: str = "fans_gender",
                          proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户粉丝兴趣"""
        data = {
            "sec_user_id": sec_user_id,
            "interest_type": interest_type,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/user_fans_interest", data)

    def aweme_digs_interest(self, aweme_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频点赞用户兴趣分析"""
        data = {
            "aweme_id": aweme_id,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/aweme_digs_interest", data)

    def hot_spot_video(self, date: int, page: int = 1, page_size: int = 30,
                       sub_type: int = 1001, root_tag: Optional[int] = None,
                       proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """抖音视频榜单"""
        data = {
            "date": date,
            "page": page,
            "page_size": page_size,
            "sub_type": sub_type,
            "root_tag": root_tag,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/hot_spot_video", data)

    def content_tag(self, content: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """内容标签分析"""
        data = {
            "content": content,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/content_tag", data)

    def monitor_user(self, sec_user_id: str, date: str,
                     proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """用户监控"""
        data = {
            "sec_user_id": sec_user_id,
            "date": date,
            "proxy": proxy
        }
        return self._make_request("/api/billboard/monitor_user", data) 