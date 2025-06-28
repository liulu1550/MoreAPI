from .Auth import Auth
from typing import Optional, Dict, Any, Union


class Bilibili(Auth):
    """哔哩哔哩API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    def video_data(self, bvid: Optional[str] = None, avid: Optional[str] = None,
                   proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情 - bvid和avid必填一项"""
        data = {
            "bvid": bvid,
            "avid": avid,
            "proxy": proxy
        }
        return self._make_request("/api/bilibili/video_data", data)

    def video_data_v2(self, bvid: Optional[str] = None, avid: Optional[str] = None,
                      proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频详情v2 - bvid和avid必填一项"""
        data = {
            "bvid": bvid,
            "avid": avid,
            "proxy": proxy
        }
        return self._make_request("/api/bilibili/video_data_v2", data)

    def comments(self, bvid: Optional[str] = None, avid: Optional[str] = None,
                 pn: int = 1, ps: int = 20, sort: str = "0",
                 proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取视频评论 - bvid和avid必填一项"""
        data = {
            "bvid": bvid,
            "avid": avid,
            "pn": pn,
            "ps": ps,
            "sort": sort,
            "proxy": proxy
        }
        return self._make_request("/api/bilibili/comments", data)

    def video_download(self, bvid: Optional[str] = None, avid: Optional[str] = None,
                       cid: Optional[str] = None, proxy: Union[str, bool, None] = None,
                       cookie: Optional[str] = None) -> Dict[str, Any]:
        """视频下载链接获取 - bvid和avid必填一项"""
        data = {
            "bvid": bvid,
            "avid": avid,
            "cid": cid,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/bilibili/video_download", data, headers)

    def video_download_v2(self, bvid: Optional[str] = None, avid: Optional[str] = None,
                          cid: Optional[str] = None, proxy: Union[str, bool, None] = None,
                          cookie: Optional[str] = None) -> Dict[str, Any]:
        """视频下载链接获取v2 - bvid和avid必填一项"""
        data = {
            "bvid": bvid,
            "avid": avid,
            "cid": cid,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/bilibili/video_download_v2", data, headers)

    def user_post(self, uid: str, pn: int = 1, ps: int = 30,
                  proxy: Union[str, bool, None] = None,
                  cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户投稿"""
        data = {
            "uid": uid,
            "pn": pn,
            "ps": ps,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/bilibili/user_post", data, headers)

    def user_post_v2(self, uid: str, pn: int = 1, ps: int = 30,
                     proxy: Union[str, bool, None] = None,
                     cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户投稿v2"""
        data = {
            "uid": uid,
            "pn": pn,
            "ps": ps,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/bilibili/user_post_v2", data, headers)

    def user_info(self, uid: str, proxy: Union[str, bool, None] = None,
                  cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户信息"""
        data = {
            "uid": uid,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/bilibili/user_info", data, headers)

    def user_videos(self, uid: str, keyword: str = "", tid: str = "0", 
                    order: str = "pubdate", pn: int = 1, ps: int = 30,
                    proxy: Union[str, bool, None] = None, 
                    cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户投稿视频"""
        data = {
            "uid": uid,
            "keyword": keyword,
            "tid": tid,
            "order": order,
            "pn": pn,
            "ps": ps,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/bilibili/user_videos", data, headers)

    def search(self, keyword: str, search_type: str = "VIDEO", 
               order_type: str = "TOTALRANK", order_sort: str = "0",
               time_range: int = -1, page: int = 1, 
               proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """搜索数据"""
        data = {
            "keyword": keyword,
            "search_type": search_type,
            "order_type": order_type,
            "order_sort": order_sort,
            "time_range": time_range,
            "page": page,
            "proxy": proxy
        }
        return self._make_request("/api/bilibili/search", data) 