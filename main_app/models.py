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

class Post(models.Model):
    caption = models.CharField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.caption} {self.date}"

    def get_absolute_url(self): 
        return reverse('post_detail', kwargs={'post_id': self.id})
    
    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    content = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.content}"
    
    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date']
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ManyToManyField(Post, related_name='likes')
    def __str__(self):
        return f"{self.user.profile.username}/{self.post}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='photo')

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    def __str__(self):
        return f"user{self.follower} followed user:{self.following}"

    def get_absolute_url(self):
        return reverse('home')