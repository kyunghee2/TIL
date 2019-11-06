from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 표시 형식 
    def __str__(self):
         return f'[{self.pk}번글]: {self.title}|{self.content}'