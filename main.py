"""
Motor Image Collector
主程序入口
Version 1.0
"""

import sys

from PySide6.QtWidgets import QApplication, QLabel, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Motor Image Collector")

        self.resize(600, 400)

        label = QLabel(
            "Motor Image Collector\n\n"
            "CFMOTO 官方图片采集工具\n\n"
            "Version 1.0",
            self
        )

        label.move(120, 120)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
