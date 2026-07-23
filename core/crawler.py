"""
官方图片搜索模块

负责：
1. 访问品牌官网
2. 查找图片链接
3. 返回图片列表
"""

import requests
from bs4 import BeautifulSoup


class ImageCrawler:

    def __init__(self, brand):
        self.brand = brand


    def search_images(self, model):

        """
        搜索车型图片

        当前版本：
        建立接口

        后续接入 CFMOTO 官方网站
        """

        print(
            f"正在搜索 {self.brand} {model}"
        )

        images = []

        return images
