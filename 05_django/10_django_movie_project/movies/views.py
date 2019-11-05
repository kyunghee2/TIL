from django.shortcuts import render,redirect
from .models import Movie
from .models import Comment
import csv
from datetime import datetime

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context ={
        'movies':movies
    }
    print(movies)
    return render(request,'movies/index.html',context)

# def new(request):
#     return render(request,'movies/new.html')

def create(request):
    if request.method =='POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie = Movie(title=title,title_en=title_en,audience=audience,open_date=open_date,genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
        movie.save()
        return redirect('movies:index')
    else:
        return render(request,'movies/create.html')

# def edit(request,movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     context = {'movie': movie}
#     return render(request,'movies/edit.html',context)

def update(request,movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()

        return redirect('movies:detail',movie_pk)
    else:
        movie = Movie.objects.get(pk=movie_pk)
        context = {'movie': movie}
        return render(request,'movies/update.html',context)

def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comment_set.all()
    context = {
        'movie':movie,
        'comments':comments
    }
    return render(request,'movies/detail.html',context)
    
def delete(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return redirect('movies:index')

def csvfilesave(request):
    with open('data.csv', newline='', encoding='UTF8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['\ufefftitle']
            title_en = row['title_en']
            audience= row['audience']
            s = row['open_date']
            date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
            open_date = date
            genre=row['genre']
            watch_grade=row['watch_grade']
            score=row['score']
            poster_url=row['poster_url']
            description=row['description']

            movie = Movie(title=title,title_en=title_en,audience=audience,open_date=open_date,genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
            movie.save()
        
    return render(request,'movies/save_result.html')

#댓글 생성
def comments_create(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(movie=movie,content=content)
        comment.save()
        return redirect('movies:detail',movie_pk)
    else:
        return redirect('movies:detail',movie_pk)

#댓글 삭제
def comments_delete(request,movie_pk,comment_pk):
    if request.method =='POST':
        movie = Comment.objects.get(pk=comment_pk)
        movie.delete()
        return redirect('movies:detail',movie_pk)
    else:
        return redirect('movies:detail',movie_pk)
