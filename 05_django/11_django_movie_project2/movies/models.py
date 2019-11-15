from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField()
    poster= models.ImageField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    #객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] {self.title}'

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    score = models.FloatField(null=True, blank=True)
    content = models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk',] #정렬설정

    def __str__(self):
        return self.content