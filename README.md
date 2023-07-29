## Description/简介

`MoreAPI`是抖音/酷我/小红书/各视频平台非官方的RESTful API平台。

`MoreAPI`提供的API只能获取公开数据，即任何人都可以通过浏览器及APP等访问相关服务以获取它们。

如果您有任何建议或者需求，请联系站长，更多的功能正在开发中，敬请期待！

文档地址：[http://doc.moreapi.wouldmissyou.com/](http://doc.moreapi.wouldmissyou.com/)

## Authorization/鉴权

`MoreAPI`为节省服务器资源，除用户模块部分接口外，皆采用请求携带特定字符进行鉴权，请求接口需要在请求头中携带Token才可调用。调用这些接口会使用你账户中的积分，每1积分可请求一次，请求失败不消耗积分！

## Announcement/公告

`MoreAPI`将使用**免费以及赞助**的形式运行。你可以通过利用 `MoreAPI`编写开源软件并且提交至GitHub，我们会在审核通过后赠送你一定的API请求次数。或者通过赞助本站，本站根据你的赞助金额赠送你一定的API请求次数。

登录后进行签到可以随机获得20-50次API请求，每天00:00重置签到。签到获得的API请求次数只有请求API才会消耗。

## Sites/站点

博客：[https://www.wouldmissyou.com](https://www.wouldmissyou.com)

QQ:1550422895

EMAIL: wouldmissyou@163.com

MoreAPI接口文档： [http://doc.moreapi.wouldmissyou.com/](http://doc.moreapi.wouldmissyou.com/)

## Plans/更新计划

如果你有好的计划请联系QQ或到博客留言。


## User/使用方法

#### 注册账号

注册地址  [http://doc.moreapi.wouldmissyou.com/api-97366881](http://doc.moreapi.wouldmissyou.com/api-97366881)

#### 调用示例

```python
import moreapi

if __name__ == '__main__':
    token = "您账号的token"  # 注册账号后登录获取token
    douyin_api = moreapi.DouYin(token)  # 抖音接口
    video_data = douyin_api.get_video_data("7258926046223797544")  # 调用获取抖音单一视频信息API
    print(video_data)
```

文档地址：[http://doc.moreapi.wouldmissyou.com/](http://doc.moreapi.wouldmissyou.com/)