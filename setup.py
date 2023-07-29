from setuptools import (setup, find_packages)

setup(

    name="MoreApi",  # 包名
    author='MoreCoding',  #作者
    version="0.2",  # 版本
    url='https://github.com/liulu1550/MoreAPI.git',  # github地址
    description='MoreAPI是抖音/酷我/小红书/快手等各视频平台非官方的RESTful API平台。',  #包的简述
    long_description=open('README.md', encoding='utf-8').read(),  # #包的详细介绍
    long_description_content_type="text/markdown",
    # 需要包含的子包列表
    packages=find_packages(),
    author_email='wouldmissyou@163.com',
    # 依赖包
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)