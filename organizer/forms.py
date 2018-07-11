from django import forms

from .models import Tag, Startup, Newslink
from .utils import SlugCleanMixin


class TagForm(SlugCleanMixin ,forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter desired tag name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter slug'
            })
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.lower()

    
class StartupForm(SlugCleanMixin ,forms.ModelForm):
    
    class Meta:
        YEARS = ['2000', '2001', '2002', '2003', '2004',
                 '2005', '2006', '2007', '2008', '2009', '2010','2011','2012','2013','2014','2015','2016','2017','2018']
        model = Startup
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'founded_date': forms.SelectDateWidget(years=YEARS),
            'contact': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
            })
        }


    
class NewslinkForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Newslink
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'pub_date':forms.SelectDateWidget,
            'link': forms.URLInput(attrs={
                'class': 'form-control'
            }),
            'startup': forms.HiddenInput()
        }
        
    
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
    
    