import hashlib
from django.contrib.auth.decorators import login_required
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
    if request.user.is_authenticated:#사용자가 로그인 되어 있는지
        article = get_object_or_404(Article,pk=article_pk) #삭제할 게시글
        if request.user == article.user: #로그인한 사용자와 게시글 작성자가 같은지
            article.delete()
        else:
            return redirect('articles:detail',article.pk)

    return redirect('articles:index')
    

def update(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.user == article.user: #작성자가 같은경우만
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()               
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)       
    else:
        return redirect('articles/index')   

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
    #article = get_object_or_404(Article, pk =article_pk)    
    comment_form = CommentForm(requset.POST)
    if comment_form.is_valid():
        comment  = comment_form.save(commit=False)
        comment.user = requset.user
        #comment.article = article    #방법1    
        comment.article_id = article_pk #방법2
        comment.save()

        return redirect('articles:detail',article_pk)

@require_POST
def comments_delete(requset, article_pk,comment_pk):
    if requset.user.is_authenticated: #로그인여부확인
        comment = get_object_or_404(Comment,pk=comment_pk)
        if requset.user == comment.user: #로그인한 사용자와 댓글 작성자가 같을 경우
            comment.delete()
    return redirect('articles:detail',article_pk)

@login_required
def like(request, article_pk):
    #게시글 가져오기
    article = get_object_or_404(Article, pk=article_pk)
    #현재 접속하고 있는 유저
    user = request.user

    #현재 게시글을 좋아요 누른 사람 목록에 현재 접속한 유저가 있을 경우 -> 좋아요 취소
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:#목록에 없을 경우 좋아요 저장
        article.like_users.add(user)
    
    return redirect('articles:index')
