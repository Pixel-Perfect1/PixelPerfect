from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=1000)
    age = models.IntegerField()
    bio =  models.CharField(max_length=500)
    
    def __str__(self):
        return self.username

    def get_absolute_url(self): 
        return reverse('home')


class Comment(models.Model):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f"{self.user_set.profile.username}: {self.content}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user_set.profile.username}"

class Post(models.Model):
    caption = models.CharField(max_length=600)
    like = models.ManyToManyField(Like, related_name='posts')
    comments = models.ManyToManyField(Comment, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='photo')

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"