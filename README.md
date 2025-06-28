## Description/简介

`MoreAPI`是抖音/快手/小红书/哔哩哔哩/YouTube/微博weibo/tiktok/Lemon8(海外版小红书)/西瓜/头条等各视频平台非官方的RESTful API平台。

`MoreAPI`提供的API只能获取公开数据，即任何人都可以通过浏览器及APP等访问相关服务以获取它们。

如果您有任何建议或者需求，请联系站长，更多的功能正在开发中，敬请期待！


文档地址：[https://ziopqu50k5.apifox.cn/](https://ziopqu50k5.apifox.cn/)

## Authorization/鉴权

`MoreAPI`为节省服务器资源，除用户模块部分接口外，皆采用请求携带特定字符进行鉴权，请求接口需要在请求头中携带Token才可调用。调用这些接口会使用你账户中的积分，每1积分可请求一次，请求失败不消耗积分！

## Announcement/公告

`MoreAPI`将使用**免费以及赞助**的形式运行。你可以通过利用 `MoreAPI`编写开源软件并且提交至GitHub，我们会在审核通过后赠送你一定的API请求次数。或者通过赞助本站，本站根据你的赞助金额赠送你一定的API请求次数。


## 功能
- 创作者API
  1. 某音视频点赞
  2. 某音视频评论
  3. 某音用户私信
  4. 某音关注用户
  5. 某音视频收藏
  6. 某红薯点赞、收藏、评论、关注、私信
- 某音API
  1. 获取视频详情
  2. 获取用户信息
  3. 获取用户主页发布
  4. 获取直播间信息
  5. 获取视频一级评论
  6. 获取视频二级评论
  7. 综合搜索
  8. 搜索用户
  9. 搜索视频
  10. 搜索直播用户
  11. 搜索话题
  12. 获取开放直播间用户列表
  13. 获取话题视频列表
  14. 获取视频弹幕
  15. 获取视频短连接
  16. 检查dou+状态
  17. 获取视频详情V2
  18. 获取用户信息v2
  19. 橱窗信息
- 快手API
  1. 获取视频详情
  2. 获取用户基本信息
  3. 获取用户主页视频
  4. 获取视频评论
  5. 获取视频子评论
  6. 搜索视频
  7. 搜索用户
  8. 获取话题相关视频
  9. 获取视频短链
  10. 获取用户基本信息V2
- 小红书API
  1. 获取笔记详情
  2. 获取用户信息
  3. 获取用户笔记
  4. 获取笔记评论
  5. 获取笔记子评论
  6. 搜索笔记
  7. 搜索用户
  8. 获取主页推荐
  9. 搜索话题
  10. 获取话题相关笔记

......
......

## 发布功能
请移步:[https://ziopqu50k5.apifox.cn/37828617f0](https://ziopqu50k5.apifox.cn/37828617f0)


## Sites/站点

博客：[https://www.wouldmissyou.com](https://www.wouldmissyou.com)

源码购买地址：[https://www.wouldmissyou.com/2023/12/01/243/](https://www.wouldmissyou.com/2023/12/01/243/)


EMAIL: wouldmissyou@163.com

MoreAPI接口文档： [https://ziopqu50k5.apifox.cn/](https://ziopqu50k5.apifox.cn/)


微信：

![contact_me_qr.png](https://api.apifox.com/api/v1/projects/3641880/resources/422815/image-preview)
## Plans/更新计划

如果你有好的计划请联系微信或到博客留言。

## User/使用方法

#### 注册账号

注册地址  [http://api.moreapi.cn/api/auth/register/](http://api.moreapi.cn/api/auth/register/)

#### 调用示例

安装SDK
```shell
pip install MoreApi
```
使用SDK
```python
import MoreAPI
if __name__ == '__main__':
    token = "你的Token"  # 注册账号后登录获取token
    douyin_api = MoreAPI.DouYin(token)  # 抖音接口
    video_data = douyin_api.aweme_data("7258926046223797544")  # 调用获取抖音单一视频信息API
    print(video_data)
```

#### 调用API

```python
import requests

url = "http://api.moreapi.cn/api/douyin/aweme_detail"

params={
    "aweme_id":"7258926046223797544",  # 视频ID（与share_text必填一项）
    "share_text": ""  # APP端视频分享文案或短连接（与aweme_id必填一项） 例：4.38 KJi:/ U@y.TY 01/11 生活可以忙碌疲惫，但心态要简单快乐！ https://v.douyin.com/iRJwHFGy/ 复制此链接，打开Dou音搜索，直接观看视频！
}
headers = {
    'Authorization': 'Bearer xxxxxx'  # 必填 。 填写通过注册获取的token
}

response = requests.request("POST", url, headers=headers, json=params)

print(response.text)

```

文档地址：[http://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d](https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d)

# MoreAPI SDK

[![PyPI version](https://badge.fury.io/py/moreapi.svg)](https://badge.fury.io/py/moreapi)
[![Python Support](https://img.shields.io/pypi/pyversions/moreapi.svg)](https://pypi.org/project/moreapi/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/moreapi/moreapi-python-sdk/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/moreapi)](https://pepy.tech/project/moreapi)

MoreAPI是一个强大的多平台社交媒体API Python SDK，支持9大主流平台，提供143个API接口，让您轻松获取社交媒体数据。

## 🚀 特性

- **🎯 多平台支持**: 抖音、小红书、快手、哔哩哔哩、微博、TikTok、Lemon8、YouTube、榜单
- **📊 143个接口**: 覆盖视频、用户、评论、搜索、直播等全场景
- **🔒 严格对照**: 所有接口参数严格按照官方文档实现
- **🌍 完美编码**: 完美支持中文字符，无编码问题
- **⚡ 高性能**: 统一的HTTP客户端，连接复用，高效稳定
- **🛡️ 类型安全**: 完整的类型注解，IDE友好

## 📦 安装

```bash
pip install moreapi
```

## 🏁 快速开始

### 基础使用

```python
from MoreAPI import DouYin, XHS, KuaiShou

# 初始化API（请替换为您的真实token）
dy = DouYin("your_api_token")
xhs = XHS("your_api_token")
ks = KuaiShou("your_api_token")

# 抖音：获取视频详情
video_info = dy.aweme_detail(aweme_id="7493493472100355362")

# 小红书：搜索笔记
notes = xhs.search_note(keyword="护肤心得", page=1)

# 快手：获取用户信息
user_info = ks.user_data(user_id="user123", cookie="your_cookie")
```

### 中文搜索示例

```python
# 完美支持中文关键词
search_results = dy.general_search(
    keyword="美食分享",
    count=12,
    publish_time="7",  # 最近一周
    content_type="0"   # 综合
)

# 搜索用户
users = dy.search_user(keyword="美妆博主")

# 话题搜索
topics = dy.search_topic(keyword="旅游攻略", count=18)
```

## 🌟 支持平台

| 平台 | 接口数量 | 主要功能 |
|------|----------|----------|
| 🎵 **抖音 (DouYin)** | 56个 | 视频详情、用户信息、搜索、评论、直播、热榜 |
| 📝 **小红书 (XHS)** | 29个 | 笔记详情、用户信息、搜索、评论、登录 |
| ⚡ **快手 (KuaiShou)** | 9个 | 视频详情、用户信息、搜索、评论 |
| 📺 **哔哩哔哩 (Bilibili)** | 10个 | 视频数据、用户信息、搜索、下载 |
| 🐦 **微博 (WeiBo)** | 10个 | 用户详情、微博内容、评论、搜索 |
| 🎬 **TikTok** | 8个 | 视频详情、用户数据、评论、搜索 |
| 🍋 **Lemon8** | 3个 | 视频详情、用户信息、用户作品 |
| 📹 **YouTube** | 5个 | 视频数据、评论、搜索、播放列表 |
| 📊 **榜单 (Billboard)** | 13个 | 各类排行榜、热门数据、用户分析 |

## 📚 详细文档

### 抖音API示例

```python
from MoreAPI import DouYin

dy = DouYin("your_token")

# 视频相关
video = dy.aweme_detail(aweme_id="video_id")
video_v3 = dy.aweme_detail_v3(share_text="分享链接")
videos = dy.multiple_aweme_detail(item_ids="[id1,id2,id3]")

# 用户相关
user = dy.user_data(sec_user_id="user_id")
user_posts = dy.user_post(sec_user_id="user_id", count=20)
user_analysis = dy.user_product_data(sec_user_id="user_id", count=30)

# 搜索功能
search_all = dy.general_search(keyword="关键词", count=12)
search_videos = dy.search_video(keyword="视频", count=18)
search_users = dy.search_user(keyword="用户")
search_music = dy.search_music(keyword="音乐")

# 评论功能
comments = dy.video_comment(aweme_id="video_id", count=20)
sub_comments = dy.video_sub_comment(aweme_id="video_id", comment_id="comment_id")

# 直播相关
live_room = dy.live_room_data(web_rid="room_id")
live_users = dy.live_user_data(web_rid="room_id")
```

### 小红书API示例

```python
from MoreAPI import XHS

xhs = XHS("your_token")

# 笔记相关
note = xhs.note_detail(note_id="note_id", xsec_token="token")
note_v2 = xhs.note_detail_v2(share_text="分享链接")
note_comments = xhs.note_comment(note_id="note_id")

# 用户相关
user = xhs.user_detail(user_id="user_id")
user_posts = xhs.user_post(user_id="user_id", cookie="cookie")

# 搜索功能
notes = xhs.search_note(keyword="搜索词", page=1)
users = xhs.search_user(keyword="用户名")
suggestions = xhs.search_suggestion(keyword="关键词")

# 登录相关
qr_code = xhs.login_qr_code()
login_status = xhs.check_login(qr_id="qr_id", code="code")
```

## ⚙️ 高级配置

### 代理设置

```python
# HTTP代理
dy = DouYin("token")
result = dy.aweme_detail(aweme_id="id", proxy="http://proxy:8080")

# SOCKS5代理
result = dy.search_video(keyword="test", proxy="socks5://proxy:1080")

# 不使用代理
result = dy.user_data(sec_user_id="id", proxy=False)
```

### Cookie支持

```python
# 需要登录的接口
user_favorite = dy.user_favorite(
    sec_user_id="user_id",
    cookie="your_login_cookie"
)

xhs_user_posts = xhs.user_post(
    user_id="user_id", 
    cookie="xhs_cookie"
)
```

### 错误处理

```python
try:
    result = dy.aweme_detail(aweme_id="invalid_id")
except Exception as e:
    print(f"API调用失败: {e}")
    # 处理错误
```

## 🔗 获取API Token

1. 访问 [MoreAPI官网](https://api.moreapi.cn)
2. 注册账号并登录
3. 在控制台获取您的API Token
4. 查看 [API文档](https://ziopqu50k5.apifox.cn/) 了解详细使用方法

## 📋 完整接口列表

<details>
<summary>点击查看所有143个接口</summary>

### 抖音API (56个)
- 视频：`aweme_detail`, `aweme_detail_v3`, `aweme_detail_v4`, `multiple_aweme_detail`, `aweme_new_fans_count`
- 用户：`user_data`, `user_data_v2`, `user_data_v3`, `user_data_v4`, `user_post`, `user_post_v3`, `user_product_data`
- 搜索：`general_search`, `search_video`, `search_user`, `search_music`, `search_topic`, `search_live`
- 评论：`video_comment`, `video_sub_comment`
- 直播：`live_room_data`, `live_room_by_id`, `live_user_data`
- 其他：`aweme_danmaku`, `user_short_link`, `hot_spot_aladdin`, `aweme_board`

### 小红书API (29个)
- 笔记：`note_detail`, `note_detail_v2`, `note_detail_v3`, `note_comment`, `note_sub_comment`
- 用户：`user_detail`, `user_detail_v2`, `user_post`
- 搜索：`search_note`, `search_user`, `search_topic`, `search_suggestion`
- 登录：`login_qr_code`, `check_login`, `login_code`
- 已登录：`me`, `likes`, `connections`

### 其他平台接口请查看源码...
</details>

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 📞 联系我们

- 官网：https://api.moreapi.cn
- 文档：https://ziopqu50k5.apifox.cn/
- 邮箱：support@moreapi.cn
- GitHub：https://github.com/moreapi/moreapi-python-sdk

---

⭐ 如果这个项目对您有帮助，请给我们一个Star！