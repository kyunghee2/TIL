from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
from .models import Rating
from django.views.decorators.http import require_POST
from .forms import RatingForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context ={
        'movies':movies
    }
    return render(request,'movies/index.html',context)

def new(request):
    if request.method =='POST':        
        title = request.POST.get('title')
        poster = request.FILES.get('poster')
        description = request.POST.get('description')

        movie = Movie(user=request.user,title=title,poster=poster,description=description)
        movie.save()
        return redirect('movies:index')
    else:
        return render(request,'movies/create.html')


def edit(request,movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.title = request.POST.get('title')
        movie.poster = request.FILES.get('poster')
        movie.description = request.POST.get('description')
        movie.save()

        return redirect('movies:detail',movie_pk)
    else:
        movie = Movie.objects.get(pk=movie_pk)
        context = {'movie': movie}
        return render(request,'movies/update.html',context)

def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    rating_form = RatingForm()
    ratings = movie.rating_set.all()

    context = {
        'movie':movie,
        'ratings':ratings,    
        'rating_form':rating_form,    
    }
    
    return render(request,'movies/detail.html',context)
    
def delete(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return redirect('movies:index')

@require_POST
def rating_create(requset, movie_pk):
    #article = get_object_or_404(Article, pk =article_pk)    
    rating_form = RatingForm(requset.POST)
    if rating_form.is_valid():
        rating = rating_form.save(commit=False)
        rating.user = requset.user
        rating.movie_id = movie_pk 
        rating.save()

        return redirect('movies:detail',movie_pk)

@require_POST
def ratings_delete(requset, movie_pk,rating_pk):
    if requset.user.is_authenticated: #로그인여부확인
        rating = get_object_or_404(Rating,pk=rating_pk)
        if requset.user == rating.user: #로그인한 사용자와 댓글 작성자가 같을 경우
            rating.delete()
    return redirect('movies:detail',movie_pk)