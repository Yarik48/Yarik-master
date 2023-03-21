from django.forms import ModelForm, TextInput, Select
from .models import Post
from django import forms



class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'day']

        widgets = {
            'text': TextInput(attrs={'class':'form-control'}),
            'day': Select(attrs={'class':'form-control'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'day']