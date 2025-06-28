from .Auth import Auth
from typing import Optional, Dict, Any, Union


class Lemon8(Auth):
    """Lemon8 API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    def aweme_detail(self, aweme_id: Optional[str] = None, share_text: Optional[str] = None,
                     proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取作品详情 - aweme_id和share_text必填一项"""
        data = {
            "aweme_id": aweme_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/lemon/aweme_detail", data)

    def user_detail(self, user_id: Optional[str] = None, share_text: Optional[str] = None,
                    proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户信息 - user_id和share_text必填一项"""
        data = {
            "user_id": user_id,
            "share_text": share_text,
            "proxy": proxy
        }
        return self._make_request("/api/lemon/user_detail", data)

    def user_post(self, user_id: str, cursor: str = "", 
                  proxy: Union[str, bool, None] = None) -> Dict[str, Any]:
        """获取用户发布列表"""
        data = {
            "user_id": user_id,
            "cursor": cursor,
            "proxy": proxy
        }
        return self._make_request("/api/lemon/user_post", data) 