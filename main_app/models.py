from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

class Post(models.Model):
    image = models.CharField(max_length=1000)
    caption = models.CharField(max_length=600)
    likes = models.ManyToManyField(Like, related_name='posts')
    comments = models.ManyToManyField(Comment, related_name='posts')



# Create your models here.

