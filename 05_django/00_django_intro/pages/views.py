from django.shortcuts import render
import random
# Create your views here.
# view 함수 -> 중간관리자
# 사용자가 접속해서 볼 페이지를 작성. 즉 하나하나의 페이지를 view라고 부른다
# view 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다
def index(request): #첫번째 인자 반드시 request
    return render(request,'index.html') #첫번째 인자 반드시 request

def dinner(request):
    menu = ['초밥','삼겹살','치즈돈까스','살치살스테이크']
    pick = random.choice(menu)
    context = {
        'pick':pick
    }
    return render(request, 'dinner.html',context)

# Lorem Picsum  사용해서 랜덤 이미지 보여주는 페이지 만들기
def image(request):
    context ={
        'width': 250,
        'height':250
    }
    return render(request, 'image.html',context)

def hello(request, name):
    menu = ['초밥','삼겹살','치즈돈까스','살치살스테이크']
    pick = random.choice(menu)    
    context = {
        'name':name,
        'pick':pick
    }
    return render(request,'hello.html',context)

#실습1 : 템플릿 변수를 2개 이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해보자
def introduce(request):    
    context = {
        'name': '감자',
        'age':20,
        'hobby':'독서'
    }
    #render 메서드의 세번째 인자로 딕셔너리 형태로 변수를 넘길 수 있다
    return render(request,'introduce.html',context)

#실습2 : 숫자 2개를 동적 라우팅으로 전달 받아서, 두개의 숫자를 곱해주는 페이지를 만들자
def times(request,number1,number2):
    result = int(number1)*int(number2)
    context = {
        'number1':number1,
        'number2':number2,
        'result':result
    }
    return render(request,'times.html',context)

#실습3 : 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자
def area(request,radius):
    result = round((radius ** 2) * 3.141592,2)
    context = {
        'result':result
    }
    return render(request,'area.html',context)
    