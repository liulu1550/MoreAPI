import requests


class Auth:

    def __init__(self, token: str, domain: str = "https://pro.moreapi.wouldmissyou.com"):
        self.token = token  # Token/token
        self.domain = domain  # 域名/domain
        self.headers = {'Authorization': f'Bearer {token}'}



