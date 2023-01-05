from django.forms import ModelForm
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
                'content': forms.Textarea(attrs={'rows':4, 'cols':15}),
            }
