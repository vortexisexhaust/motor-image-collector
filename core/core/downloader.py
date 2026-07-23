"""
图片下载模块

负责：
1. 下载图片
2. 保存文件
3. 自动重试
"""

import os
import requests


class ImageDownloader:


    def __init__(self, save_path="output"):

        self.save_path = save_path

        os.makedirs(
            self.save_path,
            exist_ok=True
        )


    def download(
            self,
            url,
            filename
    ):

        """
        下载单张图片
        """

        filepath = os.path.join(
            self.save_path,
            filename
        )


        try:

            response = requests.get(
                url,
                timeout=20
            )


            response.raise_for_status()


            with open(
                filepath,
                "wb"
            ) as f:

                f.write(
                    response.content
                )


            print(
                f"下载完成: {filename}"
            )


            return filepath


        except Exception as e:


            print(
                f"下载失败: {e}"
            )


            return None
