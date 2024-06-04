## Description/简介
`MoreAPI_Pro`版本已发布！增加抖音6神算法！某红薯发布接口已推出！
`MoreAPI`是抖音/快手/小红书/哔哩哔哩/YouTube/微博weibo/tiktok等各视频平台非官方的RESTful API平台。

`MoreAPI`提供的API只能获取公开数据，即任何人都可以通过浏览器及APP等访问相关服务以获取它们。

如果您有任何建议或者需求，请联系站长，更多的功能正在开发中，敬请期待！

文档地址：[http://doc.moreapi.wouldmissyou.com/](http://doc.moreapi.wouldmissyou.com/)

MoreAPI_PRO接口文档：[https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d](https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d)

## Authorization/鉴权

`MoreAPI`为节省服务器资源，除用户模块部分接口外，皆采用请求携带特定字符进行鉴权，请求接口需要在请求头中携带Token才可调用。调用这些接口会使用你账户中的积分，每1积分可请求一次，请求失败不消耗积分！

## Announcement/公告

`MoreAPI`将使用**免费以及赞助**的形式运行。你可以通过利用 `MoreAPI`编写开源软件并且提交至GitHub，我们会在审核通过后赠送你一定的API请求次数。或者通过赞助本站，本站根据你的赞助金额赠送你一定的API请求次数。

登录后进行签到可以随机获得20-50次API请求，每天00:00重置签到。签到获得的API请求次数只有请求API才会消耗。

## 售价
`MoreAPI`经赞助者商榷，可对外授权源码，源码无加密。源码功能包含目前`MoreAPI`所有接口功能，并保证免费技术支持。`MoreAPI`源码购买地址：[点击购买](https://www.wouldmissyou.com/2023/12/01/243/)

## 功能
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


## Sites/站点

博客：[https://www.wouldmissyou.com](https://www.wouldmissyou.com)

源码购买地址：[https://www.wouldmissyou.com/2023/12/01/243/](https://www.wouldmissyou.com/2023/12/01/243/)

QQ:1550422895

EMAIL: wouldmissyou@163.com

MoreAPI接口文档： [http://doc.moreapi.wouldmissyou.com/](http://doc.moreapi.wouldmissyou.com/)

MoreAPI_PRO接口文档：[https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d](https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d)
微信：

![contact_me_qr.png](https://api.apifox.com/api/v1/projects/3641880/resources/422815/image-preview)
## Plans/更新计划

如果你有好的计划请联系QQ或到博客留言。

## User/使用方法

#### 注册账号

注册地址  [https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d](https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d)

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

url = "https://pro.moreapi.wouldmissyou.com/api/douyin/aweme_detail"

params={
    "aweme_id":"7258926046223797544",  # 视频ID（与share_text必填一项）
    "share_text": ""  # APP端视频分享文案或短连接（与aweme_id必填一项） 例：4.38 KJi:/ U@y.TY 01/11 生活可以忙碌疲惫，但心态要简单快乐！ https://v.douyin.com/iRJwHFGy/ 复制此链接，打开Dou音搜索，直接观看视频！
}
headers = {
    'Cookie': '',  # 选填
    'Authorization': 'Bearer xxxxxx'  # 必填 。 填写通过注册获取的token
}

response = requests.request("POST", url, headers=headers, json=params)

print(response.text)

```

文档地址：[https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d](https://apifox.com/apidoc/shared-0b55c993-4634-4f70-b6fc-3edf1c27344d)