from django import forms
from django.utils.text import slugify

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'tag': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'startup': forms.SelectMultiple(attrs={
                'class':'form-control'
            })
        }
    
    def clean(self):
        cleaned_data=super().clean()
        cleaned_data['slug']=slugify(cleaned_data.get('title'))
        return cleaned_data
        
    

