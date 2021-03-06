## TerminalController
windows/Linux(理论支持Mac) 远程管理：屏幕监控（win）、键盘记录（linux 需root权限）、文件管理、命令执行
### 
    被控端逻辑代码分离，被控端连到服务器才下发逻辑代码，后期可动态更新被控端功能，而不需要重新下载编译
### 项目仍在开发中... 进度 9/10
#### 目前可以使用的功能：
    屏幕监控、键盘记录、文件管理（上传、遍历、在线编辑、删除、重命名、下载、解压缩zip）、命令执行
### 关于运行(运行的server机器需要python3.8+)
    git clone https://github.com/mycve/TerminalController.git
    cd TerminalController/server
    python -m pip install -r requirements.txt
    python server.py
    

### 关于构建客户端说明
    linux被控端:依赖python3的环境->输入服务器地址（默认为的URL）->可以直接生成在buildout目录
    windows被控端:输入服务器地址点击创建后，手动运行目录下的build.cmd，在弹出的界面（非web弹出）一直点下一步（调用win系统自带打包工具），等待打包完，到buildout目录
    你也可以使用Python打包工具（pyintaller，pyexe，nuitka等）打包二进制，修改client目录下__main__.py服务器地址如：SERVER_ADDRESS = "https://xxx.com",接着到linux、win、mac下使用例如`pyinstaller -F client/app.py` 打包可执行文件(如果你看不懂这句话，参考下面Pyinstaller)
    服务端生成被控制端需要windows机器运行server，如果不需要生成被控端，server也可以在Linux上启动
### [Pyinstaller](http://c.biancheng.net/view/2690.html)

### 关于项目结构
    buildenv打包依赖
    buildout可执行文件的输出目录
    client 被控端基础代码
    server服务端
        server.py 服务端启动入口
        config.py （全局你只需要关心这个配置文件）SPEED=3 代表截屏速度每3秒1次，最好不要小于0.7左右
        app.py 客户端待打包入口文件，打包时会复制一份到client下
        views 注册的路由逻辑代码对应后端逻辑、前端渲染页面html
        plugins 后期用于加载到客户端的插件（代码）
            core.py 客户端后期动态加载的逻辑代码
            socks5.py 用于在客户端添加socks5 代理
            portforward.py 用于转发客户端机器的端口到指定端口上（搭配socks5插件）
        model 存放定义的数据类型
        requirements.txt 服务端依赖库清单
        static 静态文件，存放对方拉回的文件，web的ui，css，js等
             files 点击下载的文件会到这里
        templates 存放web界面模板
    build.cmd windows编译可执行文件打包

### 版本更新
    【2021/11/25】 已经完成socks5的设计，可以使用
### 后期规划
    需要充足的时间构建，完成一个插件式的远程管理。
    插件可能包含（内存加载exe，socks5，扫描器等）
    这么个平台。
### gif预览
<img alt="image" height="300" src="https://github.com/mycve/TerminalController/raw/main/demo.gif" width="1400"/>

### 免责、版权声明（浏览、下载=代表同意条款）
    此工具作用于合规合法的攻防演练，或其它（包括不限于 教育、学习等目的）
    开发者享有最终解释权、任何分歧等问题、以开发者解释为准。
