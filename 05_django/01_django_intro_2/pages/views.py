from django.shortcuts import render
import requests,random

# Create your views here.
def index(request):
    return render(request,'index.html')

# 정보를 던져줄 페이지
def throw(request):
    return render(request, 'throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지
def catch(request):
    message = request.GET.get('message')
    context = {
        'message':message
    }
    return render(request, 'catch.html',context)

# [실습] 아스키 아티 API를 통한 요청-응답 실습(ASCII ARTII)
# 사용자로 부터 텍스트 입력받는 페이지
def art(request):
    return render(request,'art.html')

def art_result(request):
    word = request.GET.get('word')
    
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text    
    fonts = fonts.split('\n')  

    font = random.choice(fonts)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context ={
        'result':result
    }
    return render(request, 'art_result.html',context)

