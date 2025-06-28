from .Auth import Auth
from typing import Optional, Dict, Any, Union


class XHS(Auth):
    """小红书API类 - 严格按照接口文档实现所有接口"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        super().__init__(token, domain)

    # ===== 笔记相关接口 =====
    def note_detail(self, note_id: Optional[str] = None, xsec_token: Optional[str] = None,
                    share_text: Optional[str] = None, proxy: Optional[str] = None,
                    cookie: str = "") -> Dict[str, Any]:
        """获取笔记详情 - 需要Cookie头，note_id+xsec_token或share_text必填"""
        data = {
            "note_id": note_id,
            "xsec_token": xsec_token,
            "share_text": share_text,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/xhs/note_detail", data, headers)

    def note_detail_v2(self, note_id: Optional[str] = None, xsec_token: Optional[str] = None,
                       share_text: Optional[str] = None, proxy: Optional[str] = None,
                       cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取笔记详情v2 - Cookie可选，note_id+xsec_token或share_text必填"""
        data = {
            "note_id": note_id,
            "xsec_token": xsec_token,
            "share_text": share_text,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/note_detail_v2", data, headers)

    def note_detail_v3(self, note_id: Optional[str] = None, share_text: Optional[str] = None,
                       proxy: Optional[str] = None, cookie: str = "") -> Dict[str, Any]:
        """获取笔记详情v3 - 需要Cookie头，note_id或share_text必填一项"""
        data = {
            "note_id": note_id,
            "share_text": share_text,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/xhs/note_detail_v3", data, headers)

    def note_comment(self, note_id: str, cursor: str = "", proxy: Optional[str] = None,
                     cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取笔记父级评论"""
        data = {
            "note_id": note_id,
            "cursor": cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/note_comment", data, headers)

    def note_sub_comment(self, note_id: str, root_comment_id: str, cursor: str = "",
                         proxy: Optional[str] = None, cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取笔记子级评论"""
        data = {
            "note_id": note_id,
            "root_comment_id": root_comment_id,
            "cursor": cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/note_sub_comment", data, headers)

    def share_code(self, note_id: str, proxy: Optional[str] = None,
                   cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取笔记分享code"""
        data = {
            "note_id": note_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/share_code", data, headers)

    def short_link(self, note_id: str, proxy: Optional[str] = None,
                   cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取笔记分享短链"""
        data = {
            "note_id": note_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/short_link", data, headers)

    # ===== 用户相关接口 =====
    def user_detail(self, user_id: str, proxy: Union[str, bool, None] = None,
                    cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户详情"""
        data = {
            "user_id": user_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/user_detail", data, headers)

    def user_detail_v2(self, user_id: str, proxy: Union[str, bool, None] = None,
                       cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户详情v2"""
        data = {
            "user_id": user_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/user_detail_v2", data, headers)

    def user_post(self, user_id: str, cursor: str = "", proxy: Optional[str] = None,
                  cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取用户主页发布"""
        data = {
            "user_id": user_id,
            "cursor": cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/user_post", data, headers)

    # ===== 搜索相关接口 =====
    def search_note(self, keyword: str, page: int = 1, page_size: int = 15,
                    sort_by: str = "general", note_type: str = "0",
                    proxy: Optional[str] = None, cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索笔记"""
        data = {
            "keyword": keyword,
            "page": page,
            "page_size": page_size,
            "sort_by": sort_by,
            "note_type": note_type,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/search_note", data, headers)

    def search_user(self, keyword: str, page: int = 1, page_size: int = 15,
                    proxy: Optional[str] = None, cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索用户"""
        data = {
            "keyword": keyword,
            "page": page,
            "page_size": page_size,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/search_user", data, headers)

    def search_one_box(self, xhs_id: str, proxy: Optional[str] = None,
                       cookie: Optional[str] = None) -> Dict[str, Any]:
        """根据小红书号搜索用户"""
        data = {
            "xhs_id": xhs_id,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/search_one_box", data, headers)

    def search_topic(self, keyword: str, proxy: Optional[str] = None,
                     cookie: Optional[str] = None) -> Dict[str, Any]:
        """搜索话题"""
        data = {
            "keyword": keyword,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/search_topic", data, headers)

    def search_suggestion(self, keyword: str, proxy: Optional[str] = None) -> Dict[str, Any]:
        """获取搜索联想词"""
        data = {
            "keyword": keyword,
            "proxy": proxy
        }
        return self._make_request("/api/xhs/search_suggestion", data)

    # ===== 其他功能接口 =====
    def home_feeds(self, cursor_score: str = "", proxy: Optional[str] = None,
                   cookie: Optional[str] = None) -> Dict[str, Any]:
        """获取首页推荐"""
        data = {
            "cursor_score": cursor_score,
            "proxy": proxy
        }
        headers = {"Cookie": cookie} if cookie else None
        return self._make_request("/api/xhs/home_feeds", data, headers)

    def any_account(self, proxy: Optional[str] = None) -> Dict[str, Any]:
        """获取匿名cookie"""
        data = {
            "proxy": proxy
        }
        return self._make_request("/api/xhs/any_account", data)

    # ===== 登录相关接口 =====
    def login_qr_code(self, proxy: Optional[str] = None) -> Dict[str, Any]:
        """二维码登录 - 获取登录二维码"""
        data = {
            "proxy": proxy
        }
        return self._make_request("/api/xhs/login_qr_code", data)

    def check_login(self, qr_id: str, code: str, proxy: Optional[str] = None) -> Dict[str, Any]:
        """二维码登录 - 检查扫码结果"""
        data = {
            "qr_id": qr_id,
            "code": code,
            "proxy": proxy
        }
        return self._make_request("/api/xhs/check_login", data)

    def send_code(self, phone: str, zone: str = "86", proxy: Optional[str] = None) -> Dict[str, Any]:
        """短信登录 - 发送短信验证码"""
        data = {
            "phone": phone,
            "zone": zone,
            "proxy": proxy
        }
        return self._make_request("/api/xhs/send_code", data)

    def check_code(self, phone: str, code: str, zone: str = "86",
                   proxy: Optional[str] = None) -> Dict[str, Any]:
        """短信登录-验证短信"""
        data = {
            "phone": phone,
            "code": code,
            "zone": zone,
            "proxy": proxy
        }
        return self._make_request("/api/xhs/check_code", data)

    def login_code(self, phone: str, code: str, zone: str = "86",
                   proxy: Optional[str] = None) -> Dict[str, Any]:
        """短信登录-登录"""
        data = {
            "phone": phone,
            "code": code,
            "zone": zone,
            "proxy": proxy
        }
        return self._make_request("/api/xhs/login_code", data)

    def login_code_verify_qr(self, phone: str, proxy: Optional[str] = None) -> Dict[str, Any]:
        """短信登录-获取验证二维码"""
        data = {
            "phone": phone,
            "proxy": proxy
        }
        return self._make_request("/api/xhs/login_code_verify_qr", data)

    def login_code_verify_query(self, verify_uuid: str, proxy: Optional[str] = None) -> Dict[str, Any]:
        """短信登录-验证扫码结果"""
        data = {
            "verify_uuid": verify_uuid,
            "proxy": proxy
        }
        return self._make_request("/api/xhs/login_code_verify_query", data)

    # ===== 已登录用户接口 =====
    def me(self, proxy: Optional[str] = None, cookie: str = "") -> Dict[str, Any]:
        """获取已登录的用户信息"""
        data = {
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/xhs/me", data, headers)

    def me_v2(self, proxy: Optional[str] = None, cookie: str = "") -> Dict[str, Any]:
        """获取已登录的用户信息v2"""
        data = {
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/xhs/me_v2", data, headers)

    def mentions(self, cursor: str = "", proxy: Optional[str] = None,
                 cookie: str = "") -> Dict[str, Any]:
        """获取已登录的用户的评论和@列表"""
        data = {
            "cursor": cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/xhs/mentions", data, headers)

    def likes(self, cursor: str = "", proxy: Optional[str] = None,
              cookie: str = "") -> Dict[str, Any]:
        """获取已登录的用户的赞和收藏"""
        data = {
            "cursor": cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/xhs/likes", data, headers)

    def connections(self, cursor: str = "", proxy: Optional[str] = None,
                    cookie: str = "") -> Dict[str, Any]:
        """获取已登录的用户的新增关注"""
        data = {
            "cursor": cursor,
            "proxy": proxy
        }
        headers = {"Cookie": cookie}
        return self._make_request("/api/xhs/connections", data, headers) 