from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body','slug', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }