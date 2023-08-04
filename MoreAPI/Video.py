import requests
from MoreAPI.Auth import Auth


class Video(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.video_data_url = self.domain + "/api/video/"

    def get_video_data(self, share_text: str):
        """
        抖音、快手、小红书、哔哩哔哩、西瓜、头条。。。。
        :param share_text: 短视频分享链接或网页链接
        :return:
        """
        result = requests.get(url=self.video_data_url, headers=self.headers, params={"share_text": share_text})
        return result.json()



