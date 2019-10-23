## 2019.10.23

### Python
- vs code 실행
- extentions >  python 설치
- python_practice.py 생성
```python
'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str = input('문자를 입력하세요: ')

# 아래에 코드를 작성해 주세요.
print(f'첫번째 글자는 {str[0]}')
print(str[0])
print(str[-1])

'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''
print("====================")
numbers = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.
for x in range(1,numbers+1):
    print(x)

'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.
if(number%2):
    print("홀수")
else:
    print("짝수")

#두번째
if(number%2==0):
    print("짝수 입니다.")
else:
    print("홀수 입니다.")

'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

# 아래에 코드를 작성해 주세요.
if a >= 90 and b >80 and c>80 and d>=80:
    print("True")
else:
    print("False")


'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')

# 아래에 코드를 작성해 주세요.
#.split() 
pricelist = prices.split(";")

pricelist.sort(reverse=True)
#print(pricelist)
for x in pricelist:
    print(x)
    
```
## 1. Start Flask
### 1.0 가상환경 실행
```cmd
#기본 사용법
$ python -m venv 가상환경이름
$ python -m venv venv

#가상환경 실행및 종료
$ venv ~/venv/Scripts/activate #for Windows
$ venv ~/venv/bin/activate #for Mac

#가상환경 종료
$ deactivate
```

![flask1](https://user-images.githubusercontent.com/33045725/67356386-f66fd580-f594-11e9-9c3f-9e1825eb6c68.JPG)



### 1.1 Install

-  첫 시작은 공식문서 참고하기(https://flask.palletsprojects.com/en/1.1.x/api/)
-  flask 설치
```cmd
#작업폴더 위치에서
source ~/venv/Scripts/activate #가상환경 실행
pip install flask #flask 설치
python -m pip install --upgrade pip
```

### 1.2 개발용 서버 실행
- flask 실행
```cmd
cd 03_Flask/
#파일 지정해서 실행
#사용자가 지정해서 파일생성시 코드 수정시 서버 재구동 필요
#python app.py로 생성해서 실행했을경우 자동반영
FLASK_APP=hello.py flask run 
```
- 플라스크는 기본적으로 폴더에서 app.py를 실행하려고 한다
- 개발단계에서 app.py로 파일 생성 권장
- app.py 파일 생성
- debug 모드를 활성화해서 서버 새로고침을 생략 로직 추가
```python
...
#debug 모드를 활성화해서 서버 새로고침을 생략
if __name__ == '__main__':
    app.run(debug=True)
```

### 1.3 간단한 페이지 렌더링 하기
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

#debug 모드를 활성화해서 서버 새로고침을 생략
if __name__ == '__main__':
    app.run(debug=True)
```

- app.py로 생성했을경우 아래와 같이 명령어 실행 가능
```cmd
python app.py
```

### 1.4 동적 라우팅(Vaiable Routing)
- 사용자가 URL을 통해 입력한 값을 받아서 사용할 수 있다
```python
@app.route('/greeting/<string:name>')
def greeting(name):    
    return f'안녕, {name}'
```

### 1.5 Render Template
- 템플릿을 미리 만들어 두고 사용자에게 보여줄 수 있다
- python  코드에 render_template import
```python
from flask import Flask, render_template
app = Flask(__name__)
```

- templates 폴더 생성 
- index.html 생성
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>템플릿 입니다.</h1>
  <h3>제 이름은 {{html_name}} 입니다.</h3>
</body>
</html>
```
- render_template() 템플릿 호출
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('index.html',html_name=name)

#debug 모드를 활성화해서 서버 새로고침을 생략
if __name__ == '__main__':
    app.run(debug=True)
```

### 1.6 Jinja2 템플릿 엔진 활용하기
##### 세제곱을 돌려주는 cub 페이지 작성
- cube.html 추가
```html 
...
<body> 
  <h3>{{ number }}의 세제곱 값은 {{ result }}입니다.</h3>
</body>
```
- app.py cube route 로직추가
```python
#세제곱을 돌려주는 cub 페이지 작성
#사용자한테 숫자값을 받아서 세제곱한 결과를 보여주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    #return str(number ** 3)
    result = number ** 3
    return render_template('cube.html',result=result,number=number)

```

##### 영화목록 페이지 작성
- movies.html 추가
```html
<body>
  <h1>영화목록</h1>
  <ul>
  {% for movie in movies %}
    <li>{{ movie }}</li>
  {% endfor %}
</ul>
</body>
```
- app.py : movies route 로직추가
```python

@app.route('/movies')
def movies():
    movie_list = ['82년생김지영','조커','터미네이터']
    return render_template('movies.html',movies=movie_list)
```

## 2. 요청-응답(Request-Response)
- Ping : 사용자가 일정한 주소로 요청을 보내면 , 사용자가 어떠한 값을 입력할 수 있는 Form이 담겨있는 페이지를 보여준다.
- Pong : 사용자로부터 Form 입력 데이터를 받아
### 2.1 Ping Pong
- request import
```python
#request import
from flask import Flask, render_template, request
app = Flask(__name__)
```
- ping.html 추가
```html
<body>
  <form action="/pong" method="GET">
    이름: <input type="text" name="user_name" /><br>
    <input type="submit">
  </form>
</body>
```
- app.py 로직 추가
```python
#ping : 사용자로부터 입력을 받을 Form페이지를 넘겨준다
@app.route('/ping')
def ping():
    return render_template('ping.html')
```
- pong.html 추가
```html 
<body>
  <h2>{{user_name}}님 안녕하세요~ 데이터가 저희 서버로 들어왔어요</h2>
</body>
```
- app.py 로직 추가
```python
#pong : 사용자로부터 form데이터를 전달받아서 가공한다
@app.route('/pong')
def pong():
    user_name = request.args.get('user_name')
    return render_template('pong.html',user_name=user_name)
    
```
### Fake Naver
: 위 ping-pong구조에서 온전히 우리 웹 서비스 내에서 요청과 응답 프로세스를 구현했다. 하지만 사용자로부터 요청만 받은뒤 , 데이터를 처리해서 돌려주는 응답 프로세스를 다른 서버 측에 넘겨줄 수도 있다

- naver.html 추가
```html
<body>
    <form action="https://search.naver.com/search.naver">
      <input type="text" name="query">
      <input type="submit">
    </form>
</body>
```
- app.py 로직 추가
```python
#fake naver
@app.route('/naver')
def naver():
    return render_template('naver.html')
```