
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name="movies"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/',views.new,name="new"),
    path('<int:movie_pk>/', views.detail,name="detail"),
    path('<int:movie_pk>/edit/',views.edit,name="edit"),
    path('<int:movie_pk>/delete/',views.delete,name="delete"),
    path('<int:movie_pk>/ratings/',views.rating_create,name='rating_create'),
    path('<int:movie_pk>/ratings/<int:rating_pk>/delete',views.ratings_delete,name='ratings_delete'),
]
