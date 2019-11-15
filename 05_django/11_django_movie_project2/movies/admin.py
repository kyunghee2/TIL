from django.contrib import admin
from .models import Movie
from .models import Rating
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk','title','created_at','updated_at','user_id')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('pk','score','created_at','updated_at','movie_id')



admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
