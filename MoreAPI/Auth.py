import requests
import json
from typing import Optional, Dict, Any


class Auth:
    """MoreAPI认证和基础请求类"""

    def __init__(self, token: str, domain: str = "http://api.moreapi.cn"):
        self.token = token  # Token/token
        self.domain = domain  # 域名/domain
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json;charset=utf-8',
            'User-Agent': 'MoreAPI-Python-SDK/2.1.0'
        }

    def _make_request(self, endpoint: str, data: Optional[Dict[str, Any]] = None, 
                     additional_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        统一的API请求方法
        
        Args:
            endpoint: API端点
            data: 请求数据
            additional_headers: 额外的请求头
            
        Returns:
            API响应数据
        """
        url = f"{self.domain}{endpoint}"
        headers = self.headers.copy()
        
        if additional_headers:
            headers.update(additional_headers)
        
        # 确保数据正确编码
        json_data = None
        if data:
            try:
                # 将数据序列化为JSON字符串，确保使用UTF-8编码
                json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
            except (TypeError, ValueError) as e:
                raise Exception(f"数据序列化失败: {e}")
            
        try:
            # 使用data参数而不是json参数，并明确指定编码
            response = requests.post(
                url, 
                data=json_data, 
                headers=headers,
                timeout=30  # 增加超时设置
            )
            response.raise_for_status()
            
            # 确保响应使用UTF-8解码
            response.encoding = 'utf-8'
            return response.json()
            
        except requests.exceptions.Timeout:
            raise Exception("请求超时，请检查网络连接")
        except requests.exceptions.ConnectionError:
            raise Exception("连接失败，请检查网络和域名")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP错误 {response.status_code}: {response.text}")
        except requests.RequestException as e:
            raise Exception(f"API请求失败: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"响应数据解析失败: {e}")
        except UnicodeDecodeError as e:
            raise Exception(f"响应编码解析失败: {e}")

    def test_connection(self) -> bool:
        """测试连接和Token是否有效"""
        try:
            # 使用一个简单的测试接口
            test_data = {"test": "连接测试"}
            response = self._make_request("/api/test", test_data)
            return True
        except:
            return False