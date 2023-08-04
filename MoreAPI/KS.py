import requests
from MoreAPI.Auth import Auth


class KS(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.user_video_data_url = self.domain + "/api/ks/user_video_data/"
        self.video_data_url = self.domain + "/api/ks/video_data/"
        self.user_data_url = self.domain + "/api/ks/user_data/"
        self.comments_url = self.domain + "/api/ks/comments_list/"
        self.sub_comments_url = self.domain + "/api/ks/sub_comments_list/"

    def user_video_data(self, user_id: str, cursor: str="", link_text:str=""):
        """
        获取用户主页视频
        :param user_id: 用户ID
        :return:
        """
        result = requests.get(url=self.user_video_data_url, headers=self.headers, params={"user_id": user_id, "cursor":cursor, "link_text":link_text})
        return result.json()

    def video_data(self, video_id: str, link_text: str = ""):
        """
        获取视频信息
        :param video_id: 视频ID
        :return:
        """
        result = requests.get(url=self.video_data_url, headers=self.headers,
                              params={"video_id": video_id, "link_text": link_text})
        return result.json()

    def user_data(self, user_id: str, link_text: str = ""):
        """
        获取用户信息
        :param user_id: 用户ID
        :return:
        """
        result = requests.get(url=self.user_data_url, headers=self.headers,
                              params={"user_id": user_id, "link_text": link_text})
        return result.json()


    def comments(self, video_id: str, pcursor: str="", link_text:str=""):
        """
        获取用户主页视频
        :param
        :return:
        """
        result = requests.get(url=self.comments_url, headers=self.headers, params={"video_id": video_id, "pcursor":pcursor, "link_text":link_text})
        return result.json()

    def sub_comments(self, video_id: str, root_id:str, pcursor: str="", link_text:str=""):
        """
        获取用户主页视频
        :param
        :return:
        """
        result = requests.get(url=self.sub_comments_url, headers=self.headers, params={"video_id": video_id,"root_id":root_id, "pcursor":pcursor, "link_text":link_text})
        return result.json()