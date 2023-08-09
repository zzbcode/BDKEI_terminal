# -*- coding: utf-8 -*-
# 1.0版本
# #!/usr/bin/python

# # -*- coding: UTF-8 -*-
# import os

# path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'11\\')
# # print(path)

# file_version_map ={}

# for onefile in os.listdir(path):
#     if os.path.isfile(os.path.join(path,onefile)):
#         version = onefile.split('_')[1:6]
#         aa = []
#         for i in version:
#             aa.append(int(i))
#             print(aa)

#         file_version_map[tuple(aa)] = onefile

# data =sorted(file_version_map.items(),key=lambda x:x[0])   #使用哈希码大小排序
# print(data)

# with open('file-message.txt','w',encoding='utf-8') as f:
#     for version,name in data:
#         print(name,type(name))
#         f.write(name +  '\n')
# 我需要在图形化界面中添加一个新的按钮




###2.0版本  加入ui
# import os
# import requests
# from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QPixmap
# from PyQt5 import Qt


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # 创建界面元素
#         self.select_button = QPushButton('选择文件夹', self)
#         self.select_button.setGeometry(100, 100, 150, 50)
#         self.upload_button = QPushButton('上传智能体信息', self)
#         self.upload_button.setGeometry(300, 100, 150, 50)

#         # 绑定点击事件
#         self.select_button.clicked.connect(self.select_folder)
#         self.upload_button.clicked.connect(self.upload_file)

#         # 设置窗口属性
#         self.setGeometry(100, 100, 550, 300)
#         # self.setWindowTitle('智能体上传系统')

#         # 设置窗口背景
#         pixmap = QPixmap('id.png')
#         self.label = QLabel(self)
#         self.label.setPixmap(pixmap)
#         self.label.setGeometry(350, 248, 200, 52)

#     def select_folder(self):
#         # 弹出文件夹选择对话框
#         folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
#         if folder_path:
#             # 将选择的文件夹路径保存起来
#             self.folder_path = folder_path

#     def upload_file(self):
#         # 检查是否选择了文件夹
#         if not hasattr(self, 'folder_path'):
#             return

#         # 组装文件路径
#         path = os.path.join(self.folder_path, '')

#         # 上传文件
#         file_version_map = {}
#         for onefile in os.listdir(path):
#             if os.path.isfile(os.path.join(path, onefile)):
#                 version = onefile.split('_')[1:6]
#                 aa = []
#                 for i in version:
#                     aa.append(int(i))
#                 file_version_map[tuple(aa)] = onefile

#         data = sorted(file_version_map.items(), key=lambda x: x[0])

#         with open('file-message.txt', 'w', encoding='utf-8') as f:
#             for version, name in data:
#                 f.write(name + '\n')

#         upload_url = "http://127.0.0.1/"    #填写对应上传地址
#         with open("file-message.txt", "rb") as f:
#             response = requests.post(upload_url, files={"file": f})
#         if response.status_code == 200:
#             print("文件上传成功")
#         else:
#             print("文件上传失败")


# if __name__ == '__main__':
#     app = QApplication([])
#     app.setApplicationName("全时空数据库智能体上传系统")
#     app.setWindowIcon(QIcon("logo.png"))
#     window = MainWindow()
#     window.show()
#     app.exec_()



#3.0版本  链接监控程序

import json
import os
import requests
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore,QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtGui import QPixmap
from PyQt5 import Qt
import subprocess # 新增模块
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

from PyQt5.QtCore import QCoreApplication#退出

import pickle       #保存路径

from PyQt5.QtWidgets import QMessageBox,QTextBrowser #增加新功能，保存已有路径并判断




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setWindowFlag(QtCore.Qt.CustomizeWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setAutoFillBackground(True) #一定要加上
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 窗口透明
        # shadow=QGraphicsDropShadowEffect()  # 创建阴影
        # shadow.setBlurRadius(20)  # 设置阴影大小为9px
        # shadow.setColor(QColor("#444444"))  # 设置颜色透明度为100的（0,0,0）黑色
        # shadow.setOffset(0,0)  # 阴影偏移距离为0px
        # self.setGraphicsEffect(shadow)  # 添加阴影
        # self.resize(1600, 900)
        # self.setWindowFlag(QtCore.Qt.WindowType.CustomizeWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # app.setWindowFlag(Qt.CustomizeWindowHint)
        # app.setAttribute(Qt.WA_TranslucentBackground)  




        # 加载样式表
        
        
        # try:
        #     with open('style.qss', 'r', encoding='utf-8') as f:
        #         style = f.read()
        #         self.setStyleSheet(style)
        # except Exception as e:
        #     print('Error loading stylesheet:', e)




        # 创建界面元素
        self.select_button = QPushButton('选择智能体文件夹', self)
        self.select_button.setGeometry(650, 700, 150, 50)
        self.upload_button = QPushButton('上传数据', self)
        self.upload_button.setGeometry(950, 700, 150, 50)
        
        # 新增按钮
        self.monitor_button = QPushButton('建立本机服务端', self)
        self.monitor_button.setGeometry(950, 800, 150, 50)



        # 上传文件按钮
        self.up_button = QPushButton('索引系统-客户端', self)
        self.up_button.setGeometry(650, 800, 150, 50)


                # 给按钮添加图标
        self.select_button.setIcon(QIcon('photo/logo1.png'))
        self.upload_button.setIcon(QIcon('photo/logo2.png'))
        self.monitor_button.setIcon(QIcon('photo/logo3.png'))
        self.up_button.setIcon(QIcon('photo/logo4.png'))




        # 添加使用教程
        # self.usage_label_1 = QLabel("使用教程:", self)
        self.usage_label_1 = QLabel("", self)
        self.usage_label_1.setGeometry(850, 900, 100, 40)
        self.usage_label_1.setAlignment(QtCore.Qt.AlignCenter)
        #624
        # self.usage_label_1.setStyleSheet(
        # "background-color: #333; "
        # "color: white; "
        # "font-size: 20px; "
        # "font-weight: bold; "
        # "border-top-left-radius: 10px; "
        # "border-top-right-radius: 10px; "
        # "padding: 10px; "
        # )
        # self.usage_label_1.setStyleSheet(
        #     "background-color: #333; "
        #     "color: white; "
        #     "font-size: 16px; "
        #     "font-weight: bold; "
        #     "border-bottom-left-radius: 10px;"
        #     "border-bottom-right-radius: 10px; "
        #     "padding: 10px; "
        #     "line-height: 2.0;"
        # )
        # self.usage_label_1.setCursor(QCursor.setShape(QCursor.PointingHandCursor))
        self.usage_label_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.usage_label_1.setMouseTracking(True)
        self.usage_label_1.setToolTip("点击查看使用教程")

        
        
        #624
        # self.usage_label_2 = QTextBrowser(self)
        # self.usage_label_2.setGeometry(310, 260, 700, 200)
        # self.usage_label_2.setStyleSheet(
        #     "background-color: #333; "
        #     "color: white; "
        #     "font-size: 16px; "
        #     "font-weight: bold; "
        #     "border-bottom-left-radius: 10px;"
        #     "border-bottom-right-radius: 10px; "
        #     "padding: 10px; "
        #     "line-height: 2.0;"
        # )
        # self.usage_label_2.setPlainText("1. 通过选择智能体内部的子文件夹，统计对应文件夹下的文件信息。如果用户选择更新文件夹，则会弹出文件夹选择对话框，选择完成后会保存新的文件夹路径并在状态栏上显示。\n2.上传智能体信息模块可以通过令牌token认证,将智能体信息以及文件通过接口以post请求格式传送到服务器上\n3.建立本机服务端基于flask server实现两种接口接口1可以响应外界GET请求直接返回所请求的智能体文件夹信息接口2可以响应外界GET file请求，将对应的文件作为响应回传\n4.客户端用于模拟服务器或用户机请求文件的过程，通过读取生成的文件信息列表选择对应文件发送请求并下载")
        
        # 事件 - 鼠标点击弹出使用教程
        self.usage_label_1.mousePressEvent = lambda event: self.show_usage_method()


        # 绑定点击事件
        self.select_button.clicked.connect(self.select_folder)
        self.upload_button.clicked.connect(self.upload_file)
        
        # 绑定点击事件
        self.monitor_button.clicked.connect(self.run_monitor) # 新增绑定事件

        self.up_button.clicked.connect(self.up_file) # 新增绑定事件










        # 设置窗口属性
        self.setGeometry(27, 27, 1800, 1000) # 修改窗口大小
        # self.setWindowTitle('智能体上传系统')

        # # 设置窗口背景  小图标版
        # pixmap = QPixmap('photo/id.png')
        # self.label = QLabel(self)
        # self.label.setPixmap(pixmap)
        # self.label.setGeometry(0, 0, 200, 52)
 
        # 获取Qt界面的大小   全屏版
        # 获取Qt界面的大小
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()-20

        # 加载图片并设置大小
        pixmap = QPixmap('photo/background.png').scaled(width, height)

        # 创建标签并设置图片
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.setGeometry(0, 0, width, height)

        # 将标签放在最下层
        self.label.lower()



    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     pixmap = QPixmap('photo/id.png')
    #     painter.drawPixmap(self.rect(), pixmap)

    #     QMainWindow.paintEvent(self, event)




    def enterEvent(self, event):
        self.usage_label_1.setText("使用教程")
        self.usage_label_1.setToolTip("点击查看使用教程")
        self.usage_label_1.setStyleSheet(
            "background-color: #0b38c0; "
            "color: white; "
            "font-size: 16px; "
            "font-weight: bold; "
            # "border-bottom-left-radius: 10px;"
            # "border-bottom-right-radius: 10px; "
            "padding: 10px; "
            "line-height: 2.0;"
            "border: 1px solid white;"
        )

    def leaveEvent(self, event):
        self.usage_label_1.setToolTip("")
        self.usage_label_1.setStyleSheet(
                "background-color: #1ac9e0; "
                "color: white; "
                "font-size: 16px; "
                "font-weight: bold; "
                # "border-bottom-left-radius: 10px;"
                # "border-bottom-right-radius: 10px; "
                "padding: 10px; "
                "line-height: 2.0;"
        )


    def show_usage_method(self):
        usage_method = "1. 通过选择智能体内部的子文件夹，统计对应文件夹下的文件信息。如果用户选择更新文件夹，则会弹出文件夹选择对话框，选择完成后会保存新的文件夹路径并在状态栏上显示。\n\n" \
                       "2. 上传智能体信息模块可以通过令牌token认证，将智能体信息以及文件通过接口以post请求格式传送到服务器上。\n\n" \
                       "3. 建立本机服务端基于flask server实现两种接口：\n" \
                       "   - 接口1可以响应外界GET请求直接返回所请求的智能体文件夹信息。\n" \
                       "   - 接口2可以响应外界GET file请求，将对应的文件作为响应回传。\n\n" \
                       "4. 客户端用于模拟服务器或用户机请求文件的过程，通过读取生成的文件信息列表选择对应文件发送请求并下载。"

        # Example using a QMessageBox dialog
        # QMessageBox.information(self, "使用方法", usage_method)
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("使用方法")
        msg_box.setText(usage_method)
        # msg_box.setIcon(QMessageBox.NoIcon)   无图版本
        msg_box.setIconPixmap(QPixmap('photo/id.ico'))  # 有图版本
        msg_box.exec_()











    #升级功能：自动保存上一次路径，不必每次都选择
    # 读取保存的文件夹路径，如果不存在则返回None
    # def read_folder_path():
    #     try:
    #         with open('folder_path.pickle', 'rb') as f:
    #             return pickle.load(f)
    #     except FileNotFoundError:
    #         return None

    # # 将文件夹路径存储到文件中
    # # def write_folder_path(folder_path):
    # #     with open('folder_path.pickle', 'wb') as f:
    # #         pickle.dump(folder_path, f)
    # def write_folder_path(self, folder_path):
    #     with open('folder_path.pickle', 'wb') as f:
    #         pickle.dump(folder_path, f)



    #升级功能，选择文件夹后在状态栏显示，更新弹出提示框
    # def select_folder(self):
    #     # 弹出文件夹选择对话框
    #     folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
    #     if folder_path:
    #         # 将选择的文件夹路径保存起来
    #         self.folder_path = folder_path
    def select_folder(self):
        # 如果已经保存，则提示“是否更新文件夹”
        if hasattr(self, 'folder_path'):            #"has attribute"，意思是判断一个对象是否有指定的属性
            msg_box = QMessageBox()
            msg_box.setText(f"当前文件夹信息：{self.folder_path}")
            msg_box.setInformativeText("是否更新文件夹？")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.Yes)
            ret = msg_box.exec_()
            if ret == QMessageBox.Yes:
                folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
                if folder_path:
                    # 更新选择的文件夹路径
                    self.folder_path = folder_path
                    # 显示新的文件夹路径
                    self.statusBar().showMessage(f"当前文件夹信息：{self.folder_path}")
        else:
            # 弹出文件夹选择对话框
            folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
            if folder_path:
                # 将选择的文件夹路径保存起来
                self.folder_path = folder_path
                # 显示文件夹路径
                self.statusBar().showMessage(f"当前文件夹信息：{self.folder_path}")     
                # f-string 
                
            # folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
            # if folder_path:
            #     # 将选择的文件夹路径保存起来
                # self.folder_path = folder_path
                # self.write_folder_path(folder_path)
                # # 显示文件夹路径
            #     self.statusBar().showMessage(f"当前文件夹信息：{self.folder_path}")





    # def upload_file(self):
    #     # 检查是否选择了文件夹
    #     if not hasattr(self, 'folder_path'):
    #         print("未选择文件夹")
    #         return

    #     # 组装文件路径
    #     path = os.path.join(self.folder_path, '')

    #     # 上传文件
    #     file_version_map = {}
    #     for onefile in os.listdir(path):
    #         if os.path.isfile(os.path.join(path, onefile)):
    #             version = onefile.split('_')[1:6]
    #             aa = []
    #             for i in version:
    #                 aa.append(int(i))
    #             file_version_map[tuple(aa)] = onefile

    #     data = sorted(file_version_map.items(), key=lambda x: x[0])

    #     with open('file-message.txt', 'w', encoding='utf-8') as f:
    #         for version, name in data:
    #             f.write(name + '\n')

    #     # upload_url = "http://127.0.0.1/"    #填写对应上传地址
    #     # with open("file-message.txt", "rb") as f:
    #     #     response = requests.post(upload_url, files={"file": f})
    #     # if response.status_code == 200:
    #     #     print("文件上传成功")
    #     # else:
    #     #     print("文件上传失败")

    #     url = "http://10.2.45.17:8080/ky/sys/login"
    #     headers = {'Content-Type': 'application/json'}
    #     data = {'username': 'admin', 'password': '123456'}
    #     response = requests.post(url, headers=headers, data=json.dumps(data))


    #     # 解析JSON响应，获取token属性
    #     response_dict = json.loads(response.content)
    #     token = response_dict['result']['token']


    #     print("token值："+token)  # 输出token属性值

    #     # 设置请求头，包含token
    #     headers = {
    #         'authorization': 'authorization-text',
    #         'X-Access-Token': token,
    #         # 'Content-Type': 'application/octet-stream'
    #         # 'Content-Type': 'multipart/form-data'

    #     }


    #     # 设置请求体，包含要上传的文件
    #     files = {'file': open('file-message.txt', 'rb')}


        # # 发送POST请求
        # response = requests.post('http://10.2.45.17:8080/ky/KM/kmDoc/uploadDoc', headers=headers, files=files)

        # # 打印响应结果
        # print(response.text)

    def upload_file(self):
        if not hasattr(self, 'folder_path'):
            msg = QMessageBox()

            msg.setIcon(QMessageBox.Warning)

            msg.setWindowTitle("提示")

            msg.setText("未选择文件夹")

            msg.exec_()

            return

        ok = QInputDialog.getText(self, '输入服务器地址', '填入知识库服务器域名或IP地址:')

        if not ok:
            return

        server_address = ok[0]
        print(server_address)

        if not server_address:
            QMessageBox.warning(self, "提示", "请填入服务器地址", QMessageBox.Ok)

            return
        # self.textbox = QLineEdit(self)
        #
        # ok = QInputDialog.getText(self, '输入服务器地址', '填入知识库服务器域名或IP地址：')
        #
        # if not ok:
        #     return
        #
        # layout = QVBoxLayout()
        #
        # self.label = QLabel("填入总服务器域名或IP地址：")
        # layout.addWidget(self.label)
        #
        # self.textbox = QLineEdit(self)
        # layout.addWidget(self.textbox)
        #
        #
        # self.setLayout(layout)
        #
        #
        # server_address = self.textbox.text()
        #
        # # 检查是否填入服务器地址
        # if not server_address:
        #     QMessageBox.warning(self, "提示", "请填入服务器地址", QMessageBox.Ok)
        #     return
        #
        #
        #
        # if not hasattr(self, 'folder_path'):
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setWindowTitle("提示")
        #     msg.setText("未选择文件夹")
        #     msg.exec_()
        #     return
        #
        # 组装文件路径
        path = os.path.join(self.folder_path, '')

        # 上传文件

        # file_version_map字典会包含每个文件名与对应的哈希码的映射关系，以版本号的整数分段作为排序的依据   注意！这里是哈希逻辑
        file_version_map = {}
        for onefile in os.listdir(path):
            if os.path.isfile(os.path.join(path, onefile)):
                version = onefile.split('_')[1:6]
                aa = []
                for i in version:
                    aa.append(int(i))
                file_version_map[tuple(aa)] = onefile

        data = sorted(file_version_map.items(), key=lambda x: x[0])

        with open('file-message.txt', 'w', encoding='utf-8') as f:
            for version, name in data:
                f.write(name + '\n')


        # url = "http://10.2.61.137:8080/ky/sys/login"
        url = f"http://{server_address}/ky/sys/login"
        headers = {'Content-Type': 'application/json'}
        data = {'username': 'admin', 'password': '123456'}

        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            suggestion = "请检查目标主机是否开启，网络是否连接"
            QMessageBox.critical(self, "连接异常", error_message + "\n" + suggestion, QMessageBox.Ok)
            return

        # 解析JSON响应，获取token属性
        response_dict = json.loads(response.content)
        token = response_dict['result']['token']

        print("token值："+token)  # 输出token属性值

        # 设置请求头，包含token
        headers = {
            'authorization': 'authorization-text',
            'X-Access-Token': token,
            # 'Content-Type': 'application/octet-stream'
            # 'Content-Type': 'multipart/form-data'

        }

        # 设置请求体，包含要上传的文件
        files = {'file': open('file-message.txt', 'rb')}

        try:
            # 发送POST请求
            login_url = f"http://{server_address}/ky/KM/kmDoc/uploadDoc"
            response = requests.post(login_url, headers=headers, files=files)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            error_message = str(e)
            suggestion = "请检查目标主机是否开启，网络是否连接"
            QMessageBox.critical(self, "上传异常", error_message + "\n" + suggestion, QMessageBox.Ok)
            return

        # 打印响应结果
        print(response.text)





            
    # 新增函数
    def run_monitor(self):
        subprocess.Popen(["python", "flask_server.py"]) # 运行flask_server.py程序
        # subprocess.Popen(["python", "monitor.py"], creationflags=subprocess.CREATE_NO_WINDOW)  #避免黑窗口
        # QCoreApplication.quit()  # 退出当前程序



    #4.0版，添加上传文件功能：
    def up_file(self):
        subprocess.Popen(["python", "client.py"], creationflags=subprocess.CREATE_NO_WINDOW)  #  运行client.py程序


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("中南大学知识库分布式终端")
    app.setWindowIcon(QIcon("photo/id.ico"))

    # app.setWindowFlag(QtWidgets.QMainWindow.FramelessWindowHint)
    # app.setWindowFlag(Qt.CustomizeWindowHint)
    # app.setAttribute(Qt.WA_TranslucentBackground)    
        # 加载样式表
    with open('style.qss', 'r', encoding='utf-8') as f:
        app.setStyleSheet(f.read())


    window = MainWindow()
    window.show()
    app.exec_()
