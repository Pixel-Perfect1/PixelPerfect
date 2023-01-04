from django.forms import ModelForm
from .models import Comment, Post
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
                'content': forms.Textarea(attrs={'rows':4, 'cols':15}),
            }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'url']