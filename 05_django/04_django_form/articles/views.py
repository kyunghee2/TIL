import hashlib
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from .models import Article
from .models import Comment
from .forms import ArticleForm
from .forms import CommentForm

# Create your views here.
def index(request):
    #embed()
    # if request.user.is_authenticated:
    #     gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
    # else:
    #     gravatar_url = None

    articles = Article.objects.all()
    context = {'articles':articles,}
    return render(request,'articles/index.html', context)


def create(request):    
    if request.method == 'POST':
        # Binding 과정
        # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다.
        # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다. (그래서 변수에 담음)
        form = ArticleForm(request.POST)
        # embed()
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()

        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    # form으로 전달받는 형태가 2가지
    # 1. GET 요청 -> 비어있는 폼 전달
    # 2. 유효성 검증 실패 -> 에러 메세지를 포함한 채로 폼 전달
    context = {'form':form}
    return render(request,'articles/form.html', context)


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()

    context = {
        'article':article,
        'comment_form':comment_form,
        'comments':comments
        } 
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)    
    #if request.method == 'POST':    
    article.delete()
    return redirect('articles:index')
    


def update(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)       
        # form = ArticleForm(initial={
        #     'title':article.title,
        #     'content':article.content,
        # })

    # context로 전달되는 2가지 form 형식
    # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
    # 2. POST -> is_valid가 False가 리턴됬을 때, 오류 메세지를 포함해서 동작한다.
    context = {
        'form':form,
        'article':article
    }
    return render(request, 'articles/form.html', context)

@require_POST
def comments_create(requset, article_pk):
    article = get_object_or_404(Article, pk =article_pk)
    #if requset.method == 'POST':
    comment_form = CommentForm(requset.POST)
    if comment_form.is_valid():
        #save 메서드 -> 선택 인자:(기본값) commit=True
        #DB에 바로 저장되는 것을 막아준다
        comment  = comment_form.save(commit=False)
        comment.article = article
        comment.save()

        return redirect('articles:detail',article.pk)

@require_POST
def comments_delete(requset, article_pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return redirect('articles:detail',article_pk)

