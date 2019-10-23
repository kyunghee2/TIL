from flask import Flask, render_template
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

#debug 모드를 활성화해서 서버 새로고침을 생략
if __name__ == '__main__':
    app.run(debug=True)