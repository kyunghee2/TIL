from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index, name='index'),    # READ - Index
    path('create/',views.create, name='create'),   # GET(new) / CREATE(create)
    path('<int:article_pk>/',views.detail, name='detail'),     # READ - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'),     # DELETE
    path('<int:article_pk>/update/', views.update, name='update'),     # UPDATE - DB 저장
    path('<int:article_pk>/comments/',views.comments_create,name='comments_create'),
    path('<int:article_pk>/articles/<int:comment_pk>/delete',views.comments_delete,name='comments_delete')
]
