from .Auth import Auth
from typing import Optional, Dict, Any, Union


class WeiBo(Auth):
    """微博API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    def user_detail(self, uid: Optional[str] = None, share_text: Optional[str] = None,
                    proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户信息 - uid和share_text必填一项"""
        data = {
            "uid": uid,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/user_detail", data)

    def user_post(self, uid: Optional[str] = None, share_text: Optional[str] = None,
                  since_id: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户发布 - uid和share_text必填一项"""
        data = {
            "uid": uid,
            "share_text": share_text,
            "since_id": since_id,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/user_post", data)

    def user_video(self, uid: Optional[str] = None, share_text: Optional[str] = None,
                   since_id: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户视频列表 - uid和share_text必填一项"""
        data = {
            "uid": uid,
            "share_text": share_text,
            "since_id": since_id,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/user_video", data)

    def post_detail(self, mid: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取微博详情"""
        data = {
            "mid": mid,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/post_detail", data)

    def post_comment(self, mid: str, max_id: str = "", proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取微博评论"""
        data = {
            "mid": mid,
            "max_id": max_id,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/post_comment", data)

    def post_sub_comment(self, mid: str, cid: str, max_id: str = "",
                         proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取微博子评论"""
        data = {
            "mid": mid,
            "cid": cid,
            "max_id": max_id,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/post_sub_comment", data)

    def topic_detail(self, topic_id: str, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取话题详情"""
        data = {
            "topic_id": topic_id,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/topic_detail", data)

    def topic_statics(self, topic_id: str, since_id: str = "",
                      proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取话题统计"""
        data = {
            "topic_id": topic_id,
            "since_id": since_id,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/topic_statics", data)

    def short_video(self, uid: str, since_id: str = "",
                    proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户短视频"""
        data = {
            "uid": uid,
            "since_id": since_id,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/short_video", data)

    def search_data(self, keyword: str, type_id: str = "1", sort: str = "time",
                    page: int = 1, proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索数据"""
        data = {
            "keyword": keyword,
            "type_id": type_id,
            "sort": sort,
            "page": page,
            "proxy": proxy
        }
        return self._make_request("/api/weibo/search_data", data) 