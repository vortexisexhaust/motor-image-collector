"""
ZIP导出模块

功能：
将图片素材目录压缩成ZIP文件
"""

import os
import zipfile



class ZipExporter:


    def __init__(self):

        pass



    def export(
            self,
            source_folder,
            output_file
    ):

        """
        创建ZIP文件
        """

        with zipfile.ZipFile(
            output_file,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zipf:


            for root, dirs, files in os.walk(source_folder):

                for file in files:

                    filepath = os.path.join(
                        root,
                        file
                    )


                    arcname = os.path.relpath(
                        filepath,
                        source_folder
                    )


                    zipf.write(
                        filepath,
                        arcname
                    )


        return output_file
