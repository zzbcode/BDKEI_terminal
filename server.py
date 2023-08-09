import http.server
import os
import json

# 获取文件夹下的文件信息
def get_file_info(folder):
    file_info_list = []
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            file_info = {
                'filename': filename,
                'creator': os.getlogin(),
                'size': os.path.getsize(file_path),
                'path': file_path
            }
            file_info_list.append(file_info)
    return file_info_list

# 处理HTTP请求的处理程序
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # 处理GET请求
    def do_GET(self):
        if self.path == '/':
            # 返回文件夹下的文件信息
            file_info = get_file_info('/path/to/folder')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(file_info).encode('utf-8'))
        elif self.path.startswith('/files/'):
            # 处理对文件的请求
            filename = self.path[7:]
            file_path = os.path.join('/path/to/folder', filename)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    file_content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename="{}"'.format(filename))
                self.send_header('Content-Length', len(file_content))
                self.end_headers()
                self.wfile.write(file_content)
            else:
                # 文件不存在，返回404 Not Found错误消息
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 Not Found')
        else:
            # 请求的路径不支持，返回404 Not Found错误消息
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

if __name__ == '__main__':
    # 启动服务器
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    print('Starting server...')
    httpd.serve_forever()
