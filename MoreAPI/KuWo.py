import requests
from MoreAPI.Auth import Auth


class KuWo(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.music_search_url = self.domain + "/api/kuwo/search/"
        self.music_data_url = self.domain + "/api/kuwo/music/"

    def search_music_list(self, keyword: str, pn: int = 1, rn: int = 20):
        """
        酷我音乐搜索
        :param keyword: 搜索关键词
        :param pn: 页码  默认1
        :param rn: 每页条数  默认20
        :return:
        """
        result = requests.get(url=self.music_search_url, headers=self.headers,
                              params={"keyword": keyword, "pn": pn, "rn": rn})
        return result.json()

    def get_music_data(self, rid: str):
        """
        解析音乐详情
        :param rid: 音乐ID
        :return:
        """
        result = requests.get(url=self.music_data_url, headers=self.headers,
                              params={"rid": rid})
        return result.json()


if __name__ == '__main__':
    token = "62cauRzwo9nL2vK8DgtY9bCJ4nnsvYYvDROeodJIONJntkrrwVODh16z2myRnW2c"

    moreapi = KuWo(token)

    t = moreapi.get_music_data("440623")
    print(t)
