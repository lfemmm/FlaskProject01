from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list/')
def article_list():
    print(1+1)
    return '文章列表！！'

# 根据 id 查询
@app.route('/article1/<article_id>/')
def article_detail1(article_id):
    return '你请求的文章编号是：%s' % article_id
# 指定传参为整型，还可以 string,float...
@app.route('/article2/<int:article_id>/')
def article_detail2(article_id):
    return '你请求的文章编号是：%s' % article_id

# 和 string 类似，但是接受斜杠
@app.route('/article/<path:test>/')
def article_test(test):
    return '这是多路径：%s' % test
# 测试 uuid
@app.route('/u/<uuid:user_id>/')
def user_id(user_id):
    return '用户的id是：%s' % user_id
# any 指定多种路径
# /blog/<id>/   或者  /user/<id>/
@app.route('/<any(blog,user):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客的id是：%s' % id
    if url_path == 'user':
        return '用户的id是：%s' % id
# 通过 ？ 形式传递参数
#https://www.baidu.com/s?wd=uuid%E7%94%9F%E6%88%90
@app.route('/d/')
def d():
    uname = request.args.get('uname')
    psw = request.args.get('psw')
    return '用户名是：%s'%uname + '密码是：%s'%psw


#  url_for


if __name__ == '__main__':
    app.run(port=8000,debug=True)
