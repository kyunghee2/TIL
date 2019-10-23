from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/template')
def tem():
    return render_template('index.html')

@app.route('/ddd')
def ddd():
    return '안녕'

@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('index.html',html_name=name)
    #return f'안녕, {name}'

#debug 모드를 활성화해서 서버 새로고침을 생략
if __name__ == '__main__':
    app.run(debug=True)

