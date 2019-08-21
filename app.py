# 从 flask 这个包中导入 Flask 这个类
# Flask 这个类是项目的核心，以后很多操作都是基于这个类的对象
# 注册 url、注册蓝图等都是基于这个类的对象
from flask import Flask

# 创建一个 Flask 对象，传递__name__参数进去
# __name__参数的作用：
#   1、可以规定模板和静态文件的查找路径
#   2、以后一些 Flask 插件，比如 Flask-migrate、Flask-SQLAlchemy 如果报错了，那么 Flask
#      可以通过这个参数找到具体的错误位置。
app = Flask(__name__)

# @app.route：是一个装饰器
# @app.route('/app')就是讲 url 中的 / 映射到 hello_world 这个视图函数上面
# 以后访问这个网站的 / 目录的时候，会执行 hello_world 这个函数，然后将这个函数的返回值，返回给浏览器。
# http://127.0.0.1:5000/ ---> hello_world 函数
@app.route('/')
def hello_world():
    return 'Hello World!'

# http://127.0.0.1:5000/app ---> hello_app 函数
@app.route('/app')
def hello_app():
    return 'Hello app!'

# 如果这个文件是作为一个主文件运行，那么就执行 app.run() 方法
# 也就是启动这个网站
if __name__ == '__main__':
    # app.run()：Flask 中的一个测试浏览器
    # while True：
    #   listen()
    #   input()
    app.run()
