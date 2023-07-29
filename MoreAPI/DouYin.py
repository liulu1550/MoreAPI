import requests
from MoreAPI.Auth import Auth


class DouYin(Auth):
    def __init__(self, token: str):
        """
        初始化
        :param token: 登录用户的token
        """
        super().__init__(token)
        self.video_data_url = self.domain + "/api/douyin/video_data/"
        self.user_data_url = self.domain + "/api/douyin/user_data/"
        self.user_video_data_url = self.domain + "/api/douyin/user_video_data/"
        self.live_room_data_url = self.domain + "/api/douyin/live_room/"

    def get_video_data(self, aweme_id: str):
        """
        获取单一视频信息
        :param aweme_id: 视频ID
        :return:
        """
        result = requests.get(url=self.video_data_url, headers=self.headers, params={"aweme_id": aweme_id})
        return result.json()

    def get_user_data(self, sec_user_id: str):
        """
        获取抖音用户信息
        :param sec_user_id: 抖音用户sec_user_id
        :return:
        """
        result = requests.get(url=self.user_data_url, headers=self.headers, params={"sec_user_id": sec_user_id})
        return result.json()

    def get_user_video_data(self, sec_user_id: str):
        """
        获取抖音用户主页信息
        :param sec_user_id: 抖音用户sec_user_id
        :return:
        """
        result = requests.get(url=self.user_video_data_url, headers=self.headers, params={"sec_user_id": sec_user_id})
        return result.json()

    def get_live_room_data(self, web_rid: str):
        """
        获取抖音直播间信息和推流地址
        :param web_rid: 抖音直播间的web_rid，  https://live.douyin.com/348063806304   后面的数字就是web_rid
        :return:
        """
        result = requests.get(url=self.live_room_data_url, headers=self.headers, params={"sec_user_id": web_rid})
        return result.json()


if __name__ == '__main__':
    token = "62cauRzwo9nL2vK8DgtY9bCJ4nnsvYYvDROeodJIONJntkrrwVODh16z2myRnW2c"
    douyin_api = DouYin(token)

    video_data = douyin_api.get_video_data("7258926046223797544")
    user_data = douyin_api.get_user_data("MS4wLjABAAAAcmS1UJphcbKEcmAQvWC8KLIyKCmzHIMGAl4L2Jhaw9QLV0O3PwSZVJJF31erxLXu")
