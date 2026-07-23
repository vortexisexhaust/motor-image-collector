"""
Motor Image Collector
GUI 界面
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QComboBox,
    QListWidget
)

from config import BRAND, MODELS



class MainWindow(QWidget):

def start_collect(self):

    current_model = self.sender()

    print(
        "开始采集"
    )
    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Motor Image Collector"
        )

        self.resize(
            600,
            500
        )


        layout = QVBoxLayout()


        title = QLabel(
            "Motor Image Collector\n"
            "CFMOTO 官方图片采集工具"
        )


        layout.addWidget(
            title
        )


        # 品牌

        brand_label = QLabel(
            "品牌"
        )

        layout.addWidget(
            brand_label
        )


        brand_box = QComboBox()

        brand_box.addItem(
            BRAND
        )

        layout.addWidget(
            brand_box
        )


        # 系列

        series_label = QLabel(
            "系列"
        )

        layout.addWidget(
            series_label
        )


        series_box = QComboBox()


        for series in MODELS:

            series_box.addItem(
                series
            )


        layout.addWidget(
            series_box
        )


        # 车型

        model_list = QListWidget()


        for models in MODELS.values():

            for model in models:

                model_list.addItem(
                    model
                )


        layout.addWidget(
            model_list
        )


        # 按钮

        start_button = QPushButton(
            "开始采集图片"
        )

        start_button.clicked.connect(
            self.start_collect
        )
        
        layout.addWidget(
            start_button
        )


        export_button = QPushButton(
            "导出 ZIP"
        )


        layout.addWidget(
            export_button
        )


        self.setLayout(
            layout
        )



if __name__ == "__main__":

    app = QApplication(
        sys.argv
    )


    window = MainWindow()

    window.show()


    sys.exit(
        app.exec()
    )
