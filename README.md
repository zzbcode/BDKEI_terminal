# BDKEI知识库分布式终端系统

## 系统设计

- 本系统集成了三个子系统模块：本机作为智能体上传文件客户端、本机用于响应总服务器请求的智能体服务端、以及用户使用的索引系统客户端。本机服务端用于响应总服务器请求，实现分布式存储和检索，总服务器实现分布式集群管理和检索接收文件；用户的索引系统客户端用于检索并下载文件。
 
1. 本机作为智能体上传文件客户端：
- 通过封装HTTP POST请求实现文件上传功能。在上传前，该客户端会先检查用户是否选择了待上传的文件夹，并将该文件夹下的文件按照版本号从小到大排序。接着，该客户端会向目标主机发送HTTP POST请求，将排序后的文件名写入到请求体中并发送到目标主机。在发送请求之前，该客户端会通过HTTP POST请求登录目标主机，获取token属性值，并将其设置到请求头中，以保证请求的安全性。如果在发送请求的过程中发生异常，则该客户端会弹出提示框并返回。这个客户端的作用在于提高文件上传的自动化程度，简化了上传文件的流程，增强了文件上传的安全性和可靠性。
- 智能体文件信息或者论文信息既可以通过生成带时间戳的txt文件或者csv文件发送，由服务端进行解析，也可以使用统一格式的json包发送，这部分需要总服务端做好对应解析。

2. 本机服务端：
- 本机服务端采用Python的Socket编程实现，基于Flask架构实现路由，Flask架构是一种 Python Web 应用程序框架，它基于 Werkzeug Web Server Gateway Interface工具箱和 Jinja2 模板引擎构建。
- 主要功能是接收上传的文件，并将其存储在指定目录下。具体而言，本机服务端通过监听指定端口，等待外界的连接请求。并提供获取文件信息列表和获取文件的两个API接口。通过设置路由，当请求根目录“/”时，返回文件夹下的所有文件的基本信息列表；当请求其他路由时，根据请求的文件名返回对应的文件。主要提供了两个路由：
index() 函数绑定的路由 /，用于返回指定目录下的所有文件的信息列表，包括文件名、创建者、文件大小和文件路径等。
get_file(filename) 函数绑定的路由 /<path:filename>，用于返回指定文件的内容。

3. 索引系统客户端：
- 索引系统客户端采用Python的requests库实现，主要功能是检索并下载文件。具体而言，索引系统客户端通过读取本地txt文件中的上传时间和文件名，生成下拉框供用户选择下载的文件。一旦用户选择文件并点击下载，就会自动下载对应文件，并保存在桌面上，给出提示“文件下载成功“的弹窗提示。

![界面](photo/design.png)
![服务前端](photo/%E5%89%8D%E7%AB%AF.png)
## 系统运行步骤
- 为了提供用户友好的界面和高效的搜索功能，本系统采用了PyQt5+qss+图标库进行设计，使用高质量的图标和图片，为用户提供了良好的视觉体验。整个界面采用了现代化、清新的色调。下面给出从初始化到使用的整个流程：

1. 解压软件包，使用python命令下载软件所需要的依赖项，所有依赖项都以及存放在根目录下的requirement.txt文件中：```pip install·r requirement.txt```
2. 双击运行客户端  "终端3.0.exe"  文件：
3. 进入用户界面：
4. 选择文件夹模块：选择后，会将文件夹信息显示在状态栏：

5. 上传智能体信息：
- 遍历选定的文件夹，将所有文献信息记录下来，并通过与服务器通信，解析JSON响应，获取token属性，向服务器发送POST请求。
如果服务端正常连接，则会发送对应记录文献信息的文本文件，如果连接失败，在时间戳结束超时后，给出提示信息
6. 建立本机服务端：
点击“建立本机服务端”按钮后，启动服务端，持续监听端口，等待客户端连接。
并弹出服务端框架信息cmd窗口，并给出服务端访问地址和对应端口8000：

7. 索引系统-客户端：
点击“索引系统-客户端”按钮后，程序通过读取已经生成的文件信息，并弹出一个文件选择窗口，用户可以从列表中选择一个文件进行下载。
下载文件：在文件选择窗口中，用户可以选择一个文件进行下载。点击“下载”按钮后，程序会向服务端发送请求，并将服务端返回的文件数据写入到本地文件中。如果文件下载成功，则会弹出一个提示框。

![版权所有](photo/id.png)