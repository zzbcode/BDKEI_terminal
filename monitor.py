from PyQt5 import *
from watchdog.observers import Observer
from watchdog.events import *
import time
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton
from PyQt5.QtCore import QTextStream, QIODevice
from PyQt5.QtGui import QIcon



##原始版本


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# class FileEventHandler(FileSystemEventHandler):
#     def __init__(self, window):
#         self.window = window
#         FileSystemEventHandler.__init__(self)

#     def on_moved(self, event):
#         if event.is_directory:
#             print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
#         else:
#             print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

#     def on_created(self, event):
#         if event.is_directory:
#             print("directory created:{0}".format(event.src_path))
#         else:
#             print("file created:{0}".format(event.src_path))

#     def on_deleted(self, event):
#         if event.is_directory:
#             print("directory deleted:{0}".format(event.src_path))
#         else:
#             print("file deleted:{0}".format(event.src_path))

#     def on_modified(self, event):
#         if event.is_directory:
#             print("directory modified:{0}".format(event.src_path))
#         else:
#             print("file modified:{0}".format(event.src_path))

# def start_handler(window):
#     observer = Observer()
#     event_handler = FileEventHandler(window)
#     observer.schedule(event_handler,r"C:\Users\张同学\Desktop\py开发智能体监控\work2\file",True)
#     observer.start()

# app = QApplication(sys.argv)
# window = QWidget()
# button = QPushButton("Start", window)
# button.clicked.connect(lambda: start_handler(window))
# window.show()
# app.exec_()






###更新2.0版

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# from filenamesort import MainWindow

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, window):
        self.window = window
        FileSystemEventHandler.__init__(self)
        self.label = QLabel(window)
        self.label.setGeometry(100, 100, 3000, 100)
        # self.window.layout().addWidget(self.label)
        self.label.show()


    def on_moved(self, event):
        if event.is_directory:
            message = "directory moved from {0} to {1}".format(event.src_path,event.dest_path)
        else:
            message = "file moved from {0} to {1}".format(event.src_path,event.dest_path)
        self.label.setText(message)

    def on_created(self, event):
        if event.is_directory:
            message = "directory created:{0}".format(event.src_path)
        else:
            message = "file created:{0}".format(event.src_path)
        self.label.setText(message)

    def on_deleted(self, event):
        if event.is_directory:
            message = "directory deleted:{0}".format(event.src_path)
        else:
            message = "file deleted:{0}".format(event.src_path)
        self.label.setText(message)

    def on_modified(self, event):
        if event.is_directory:
            message = "directory modified:{0}".format(event.src_path)
        else:
            message = "file modified:{0}".format(event.src_path)
        self.label.setText(message)

def start_handler(window):
    # window2 =MainWindow()
    # window2.show()
    observer = Observer()
    event_handler = FileEventHandler(window)
    observer.schedule(event_handler,r".\file",True)
    observer.start()

app = QApplication(sys.argv)
app.setApplicationName("分布式监控系统")
app.setWindowIcon(QIcon("logo.png"))
window = QWidget()
window.resize(1000, 300)
button = QPushButton("开始监控", window)
# label = QLabel(window)
# label.move(100, 100)
# label.setText("Hello, world!")
button.clicked.connect(lambda: start_handler(window))
window.show()
app.exec_()







#更新3.0版


