from django.contrib import admin


# Register your models here.
from .models import Photo, Post, Profile, Comment

admin.site.register(Photo)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)