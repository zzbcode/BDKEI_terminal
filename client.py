# import requests
# import os

# # 要下载的文件路径和名称
# filename = "全时空对象_0_2_67_5_23_4_中南大学新校区.csv"
# # 服务器地址
# url = "http://localhost:8000/" + filename
# # 本地保存路径和名称
# local_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', filename)

# # 发送GET请求并保存响应
# response = requests.get(url)
# if response.status_code == 200:
#     with open(local_file_path, 'wb') as f:
#         f.write(response.content)
#     print("File saved to:", local_file_path)
# else:
#     print("File not found on server:", filename)
import os
import sys
import requests
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("论文智能索引系统")
        self.resize(400, 200)
        self.file_combo = QComboBox(self)
        self.file_combo.setGeometry(50, 50, 300, 30)
        self.download_btn = QPushButton("下载", self)
        self.download_btn.setGeometry(150, 100, 100, 30)
        self.download_btn.clicked.connect(self.download_file)
        self.load_file_names()

    def load_file_names(self):
        file_path = os.path.join(os.getcwd(), 'file-message.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_names = f.read().splitlines()
                
                self.file_combo.addItems(file_names)
        else:
            QMessageBox.warning(self, "警告", "文件file-message.txt不存在！")

    def download_file(self):
        file_name = self.file_combo.currentText()
        url = "http://localhost:8000/" + file_name
        local_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', file_name)
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_file_path, 'wb') as f:
                f.write(response.content)
            QMessageBox.information(self, "提示", "文件已下载至桌面！")
        else:
            QMessageBox.warning(self, "警告", "文件不存在！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("photo/csu.png"))

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
