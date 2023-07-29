import requests


class Auth:

    def __init__(self, token: str, domain: str = "https://moreapi.wouldmissyou.com"):
        self.token = token  # Token/token
        self.domain = domain  # 域名/domain
        self.headers = {'Authorization': f'Bearer {token}'} if 'bearer ' not in token.lower() else {
            'Authorization': token}

    # 签到
    def daily_check_in(self):
        url = f'{self.domain}/auth/daily_check_in/'
        result = requests.get(url=url, headers=self.headers)
        return result.json()

    def get_user_info(self):
        url = f'{self.domain}/auth/user_info/'
        result = requests.get(url=url, headers=self.headers)
        return result.json()


if __name__ == '__main__':
    token = "62cauRzwo9nL2vK8DgtY9bCJ4nnsvYYvDROeodJIONJntkrrwVODh16z2myRnW2c"
    auth = Auth(token)
    # r = auth.daily_check_in()
    # print(r)
    r2 = auth.get_user_info()
    print(r2)