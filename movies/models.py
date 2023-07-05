from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=10)
    # movie_set = 눈에는 안보이지만 자동생성, 1대 N 에서도 언급된 내용
    # a1.movie_set.all() 이런식으로 사용 a1.movie_set.add()

class Movie(models.Model):
    title = models.CharField(max_length=20)
    actors = models.ManyToManyField(Actor)




