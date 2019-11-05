from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    audience = models.IntegerField()
    open_date = models.TextField()
    genre = models.CharField(max_length=200)
    watch_grade = models.CharField(max_length=200)
    score = models.FloatField()
    poster_url = models.CharField(max_length=300)
    description = models.TextField()

    #객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] {self.title}'

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Model Level에서 Metadata 설정
    class Meta:
        ordering = ['-pk',] #정렬설정

    def __str__(self):
        return self.content
       