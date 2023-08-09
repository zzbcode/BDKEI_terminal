from flask import Flask, request, jsonify,send_file
import os
import datetime
from urllib.parse import quote
from werkzeug.utils import secure_filename





from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox
from flask import Flask, request, jsonify, send_file
import os
import datetime
from urllib.parse import quote
from werkzeug.utils import secure_filename
import socket
from PyQt5.QtWidgets import QApplication, QMessageBox
import threading

app = Flask(__name__)

# 获取文件夹下的所有文件信息
def get_file_info(directory):
    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            info = {
                "filename": filename,
                "creator": datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime('%Y-%m-%d %H:%M:%S'),
                "size": str(round(os.path.getsize(path) / 1024, 2)) + "KB",
                "path": os.path.abspath(path)
            }
            files.append(info)
    return files

# 设置路由，返回文件信息列表
@app.route("/")
def index():
    directory = r'.\paperFile'
    files = get_file_info(directory)
    return jsonify(files)

# 设置路由，返回文件
@app.route("/<path:filename>")
def get_file(filename):
    directory = r'.\paperFile'
    filepath = os.path.join(directory, filename)
    try:
        return send_file(filepath)
    except:
        return jsonify({"message": f"File not found: {filename}"})

def get_local_ip():
    try:
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip
    except:
        return "Unable to determine IP address"

def run_flask_app():
    app.run(host="0.0.0.0", debug=False, port=8000)

def show_qt_message_box(local_ip):
    qt_app = QApplication([])
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Flask服务器信息")
    msg_box.setWindowIcon(QIcon("photo/csu.png"))
    msg_box.setText(f"Flask服务器已启动\n局域网访问IP地址：{local_ip}\n端口：8000")
    # msg_box.setStandardButtons(QMessageBox.NoButton)
    msg_box.exec_()


if __name__ == "__main__":
    local_ip = get_local_ip()


    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    show_qt_message_box(local_ip)

















#
# app = Flask(__name__)
#
# # 获取文件夹下的所有文件信息
# def get_file_info(directory):
#     files = []
#     for filename in os.listdir(directory):
#         path = os.path.join(directory, filename)
#         if os.path.isfile(path):
#             info = {
#                 "filename": filename,
#                 # "creator": os.stat(path).st_uid,           #linux的方法
#                 # "creator": int(os.path.getctime(path)),  # get creation time on Windows
#                 "creator": datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime('%Y-%m-%d %H:%M:%S'),
#
#                 # "size": os.path.getsize(path),
#                 "size": str(round(os.path.getsize(path) / 1024, 2)) + "KB",
#                 "path": os.path.abspath(path)
#             }
#             files.append(info)
#     return files
#
# # 设置路由，返回文件信息列表
# @app.route("/")
# def index():
#     # directory = "/"
#     directory = r'.\paperFile'
#
#     files = get_file_info(directory)
#     return jsonify(files)
#
# # 设置路由，返回文件
# @app.route("/<path:filename>")
# def get_file(filename):
#     directory = r'.\paperFile'
#
#     filepath = os.path.join(directory, filename)
#     try:
#
#         return send_file(filepath)
#         # # 处理中文文件名编码问题
#         # filename_encoded = quote(filename)
#         # response = send_file(filepath)
#         # response.headers["Content-Disposition"] = f"attachment; filename*=UTF-8''{filename_encoded}"
#         # return response
#     except:
#         return jsonify({"message": f"File not found: {filename}"})
#
#
#
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0",debug=True, port=8000)











# @app.route("/file", methods=["POST"])
# def upload_file():
#     # 获取POST请求中的文件数据
#     file = request.files.get("file")
#     if not file:
#         return jsonify({"message": "No file provided"}), 400

#     # 获取文件名并安全地保存文件
#     filename = secure_filename(file.filename)
#     directory = r'C:\Users\张同学\Desktop\alastic_webserver\paperFile'
#     filepath = os.path.join(directory, filename)
#     file.save(filepath)

#     # 返回文件
#     try:
#         return send_file(filepath)
#     except:
#         return jsonify({"message": f"File not found: {filename}"}), 404