from .Auth import Auth
from typing import Optional, Dict, Any


class YouTube(Auth):
    """YouTube API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    def video_data(self, video_id: str) -> Dict[str, Any]:
        """获取视频数据"""
        data = {
            "video_id": video_id
        }
        return self._make_request("/api/youtube/video_data", data)

    def video_comment(self, video_id: str, max_results: int = 100,
                      page_token: str = "") -> Dict[str, Any]:
        """获取视频评论"""
        data = {
            "video_id": video_id,
            "max_results": max_results,
            "page_token": page_token
        }
        return self._make_request("/api/youtube/video_comment", data)

    def search_data(self, keyword: str, max_results: int = 25,
                    page_token: str = "", order: str = "relevance") -> Dict[str, Any]:
        """搜索视频"""
        data = {
            "keyword": keyword,
            "max_results": max_results,
            "page_token": page_token,
            "order": order
        }
        return self._make_request("/api/youtube/search_data", data)

    def play_list(self, channel_id: str, max_results: int = 25,
                  page_token: str = "") -> Dict[str, Any]:
        """获取播放列表"""
        data = {
            "channel_id": channel_id,
            "max_results": max_results,
            "page_token": page_token
        }
        return self._make_request("/api/youtube/play_list", data)

    def play_list_item(self, playlist_id: str, max_results: int = 25, 
                       page_token: str = "") -> Dict[str, Any]:
        """获取播放列表视频"""
        data = {
            "playlist_id": playlist_id,
            "max_results": max_results,
            "page_token": page_token
        }
        return self._make_request("/api/youtube/play_list_item", data) 