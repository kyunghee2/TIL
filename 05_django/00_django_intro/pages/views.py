from django.shortcuts import render

# Create your views here.
# view 함수 -> 중간관리자
# 사용자가 접속해서 볼 페이지를 작성. 즉 하나하나의 페이지를 view라고 부른다
# view 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다
def index(request): #첫번째 인자 반드시 request
    return render(request,'index.html') #첫번째 인자 반드시 request

def introduce(request):
    return render(request,'introduce.html')