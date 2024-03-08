import requests


class Auth:

    def __init__(self, token: str, domain: str = "https://pro.moreapi.wouldmissyou.com"):
        self.token = token  # Token/token
        self.domain = domain  # 域名/domain
        self.headers = {'Authorization': f'Bearer {token}'}

    # 签到
    def daily_check_in(self):
        url = f'{self.domain}/api/auth/daily_check_in'
        result = requests.get(url=url, headers=self.headers)
        return result.json()


