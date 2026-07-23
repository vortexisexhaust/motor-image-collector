"""
图片管理模块

功能：
1. 创建车型目录
2. 自动分类图片
3. 规范文件结构
"""

import os
import shutil


class ImageManager:


    def __init__(self, base_path="output"):

        self.base_path = base_path

        os.makedirs(
            self.base_path,
            exist_ok=True
        )


    def create_folder(
            self,
            series,
            model
    ):

        """
        创建车型目录

        示例：

        output/
          SR/
            450SR/
        """

        folder = os.path.join(
            self.base_path,
            series,
            model
        )

        os.makedirs(
            folder,
            exist_ok=True
        )

        return folder



    def organize_image(
            self,
            source,
            series,
            model,
            filename
    ):

        """
        整理图片
        """

        folder = self.create_folder(
            series,
            model
        )


        target = os.path.join(
            folder,
            filename
        )


        shutil.move(
            source,
            target
        )


        return target
