import requests
from MoreAPI.Auth import Auth


class XHS(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.get_note_by_id_url = self.domain + "/api/xhs/get_note_by_id/"
        self.get_user_info_url = self.domain + "/api/xhs/get_user_info/"
        self.get_user_notes_url = self.domain + "/api/xhs/get_user_notes/"
        self.get_note_comments_url = self.domain + "/api/xhs/get_note_comments/"
        self.get_note_sub_comments_url = self.domain + "/api/xhs/get_note_sub_comments/"
        self.search_note_by_keyword_url = self.domain + "/api/xhs/search_note_by_keyword/"

    def get_note_by_id(self, note_id: str):
        """
        根据笔记ID获取笔记详情
        :param note_id: 笔记ID
        :return:
        """
        result = requests.get(url=self.get_note_by_id_url, headers=self.headers, params={"note_id": note_id})
        return result.json()

    def get_user_info_data(self, user_id: str):
        """
        根据用户ID获取用户详情
        :param user_id: 用户ID
        :return:
        """
        result = requests.get(url=self.get_user_info_url, headers=self.headers, params={"user_id": user_id})
        return result.json()

    def get_user_notes(self, user_id: str, cursor: str = None, type: str = None):
        """
        获取用户笔记
        :param user_id: 用户ID
        :param cursor: 下一页参数 默认为空表示第一页
        :param type: 类型。默认为空获取用户发布的笔记。（collect:获取用户收藏笔记，like:获取用户点赞笔记）
        :return:
        """
        result = requests.get(url=self.get_user_notes_url, headers=self.headers,
                              params={"user_id": user_id, "cursor": cursor, "type": type})
        return result.json()

    def get_note_comments(self, note_id: str, cursor: str = None):
        """
        获取笔记评论
        :param note_id: 笔记ID
        :param cursor: 页码参数
        :return:
        """
        result = requests.get(url=self.get_note_comments_url, headers=self.headers,
                              params={"note_id": note_id, "cursor": cursor})
        return result.json()

    def get_note_sub_comments(self, note_id: str, root_comment_id: str, cursor: str = None, num: int = 10):
        """
        获取笔记评论下的子评论
        :param note_id: 笔记ID
        :param root_comment_id: 父级评论ID
        :param cursor: 下一页参数
        :param num: 当前页条数（默认10）
        :return:
        """
        result = requests.get(url=self.get_note_sub_comments_url, headers=self.headers,
                              params={"note_id": note_id, "root_comment_id": root_comment_id, "cursor": cursor,
                                      "num": num})
        return result.json()

    def search_note_by_keyword(self, keyword: str, page: int = 1, page_size: int = 20, sort: str = "general",
                               note_type: str = "all"):
        """
        根据关键词获取笔记列表
        :param keyword: 关键词
        :param page: 页码（默认1）
        :param page_size: 每页条数（默认20）
        :param sort: 排序方式。general:默认, hot:最热, new:最新
        :param note_type: 搜索结果类型（默认all）。all:全部,video:视频, image:图集
        :return:
        """
        result = requests.get(url=self.search_note_by_keyword_url, headers=self.headers,
                              params={"keyword": keyword, "page": page, "page_size": page_size, "sort": sort,
                                      "note_type": note_type})
        return result.json()


if __name__ == '__main__':
    token = "62cauRzwo9nL2vK8DgtY9bCJ4nnsvYYvDROeodJIONJntkrrwVODh16z2myRnW2c"

    moreapi = XHS(token)

    # t = moreapi.get_note_by_id("64bdf819000000001201a397")
    # print(t)

    # t = moreapi.get_user_info_data("61dbbe4e000000002102591f")
    # print(t)

    t = moreapi.get_user_notes("5c49ff350000000012011a11")
    print(t)
