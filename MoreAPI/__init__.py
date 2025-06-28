"""MoreAPI - 多平台社交媒体数据API Python SDK

支持平台:
- 抖音 (DouYin)
- 小红书 (XHS)
- 快手 (KuaiShou)
- 哔哩哔哩 (Bilibili)
- 微博 (WeiBo)
- TikTok
- Lemon8
- YouTube
- 榜单API (Billboard)

"""

from .Auth import Auth
from .DouYin import DouYin
from .XHS import XHS
from .KuaiShou import KuaiShou
from .Bilibili import Bilibili
from .WeiBo import WeiBo
from .TikTok import TikTok
from .Lemon8 import Lemon8
from .YouTube import YouTube
from .Billboard import Billboard

__version__ = "0.5.2"
__author__ = "MoreAPI Team"
__email__ = "wouldmissyou@163.com"
__description__ = "`MoreAPI`是抖音/快手/小红书/哔哩哔哩/YouTube/微博weibo/tiktok/Lemon8(海外版小红书)/西瓜/头条等各视频平台非官方的RESTful API平台。"

__all__ = [
    "Auth",
    "DouYin",
    "XHS",
    "KuaiShou",
    "Bilibili",
    "WeiBo",
    "TikTok",
    "Lemon8",
    "YouTube",
    "Billboard"
]

# API接口统计
API_COUNTS = {
    "抖音": 56,
    "小红书": 29,
    "快手": 9,
    "哔哩哔哩": 10,
    "微博": 10,
    "TikTok": 8,
    "Lemon8": 3,
    "YouTube": 5,
    "榜单": 13
}

TOTAL_APIS = sum(API_COUNTS.values())  # 143个接口

print(f"MoreAPI SDK v{__version__} 已加载")
print(f"支持 {len(API_COUNTS)} 个平台，共 {TOTAL_APIS} 个API接口")


