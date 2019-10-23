from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html',html_name=name)
    #return f'안녕, {name}'

#세제곱을 돌려주는 cub 페이지 작성
#사용자한테 숫자값을 받아서 세제곱한 결과를 보여주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    #return str(number ** 3)
    result = number ** 3
    return render_template('cube.html',result=result,number=number)

@app.route('/movies')
def movies():
    movie_list = ['82년생김지영','조커','궁예']
    return render_template('movies.html',movies=movie_list)

#ping : 사용자로부터 입력을 받을 Form페이지를 넘겨준다
@app.route('/ping')
def ping():
    return render_template('ping.html')

#pong : 사용자로부터 form데이터를 전달받아서 가공한다
@app.route('/pong')
def pong():
    user_name = request.args.get('user_name')
    return render_template('pong.html',user_name=user_name)

#fake naver
@app.route('/naver')
def naver():
    return render_template('naver.html')

#debug 모드를 활성화해서 서버 새로고침을 생략
if __name__ == '__main__':
    app.run(debug=True)