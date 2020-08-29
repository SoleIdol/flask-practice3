# author:Sole_idol
# filename: manage.py
# datetime:2020/8/19 7:59
'''
本程序是为了测试
语法练习post、get
'''
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=('POST', 'GET'))
def main():
    print(request.method)
    if request.method == 'POST':  # 这里POST要大写
        file = request.files.get('file')
        if file != None:
            # print(file.filename)
            file.save(f'static/upload/{file.filename}')
            return redirect('/redir/')  # 跳转路由
    else:
        return render_template('main.html')


@app.route('/redir/', methods=('POST', 'GET'))
def redirect1():
    return render_template('red.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
