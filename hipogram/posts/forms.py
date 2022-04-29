from django import forms
from hipogram.posts.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'text']
