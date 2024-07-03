import requests


class CustomSDKException(Exception):
    pass

def post_request(url: str, json_data: dict, headers: dict):
    """
    封装的HTTP POST请求方法
    :param url: 请求的URL
    :param json_data: JSON格式的请求数据
    :param headers: 请求头
    :return: 响应结果
    :raises CustomSDKException: 如果请求失败或响应状态码不是200，则抛出异常
    """
    try:
        response = requests.post(url, json=json_data, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是200，则抛出异常
        return response.json()  # 返回JSON格式的响应结果
    except requests.HTTPError as e:
        raise CustomSDKException(f"HTTP错误: {e.response.status_code}, 响应内容: {e.response.text}")
    except Exception as e:
        raise CustomSDKException(f"请求过程中发生错误: {e}")
