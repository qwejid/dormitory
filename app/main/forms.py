
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddPostForm(forms.ModelForm):
    
       
    class Meta:
        model = News
        fields = ['title', 'text', 'image']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'field__input', 'placeholder':'Монополия'}),
            'text' : forms.Textarea(attrs={'class':'field__input auto-resize-textarea', 'placeholder':'Сегодня собираемся для игры в ...'}),
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 200:
                raise forms.ValidationError('Длина превышает 200 символов')
            return title
        

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'cat_prod', 'price', 'link']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'field__input', 'placeholder':'Стол'}),
            'price' : forms.TextInput(attrs={'class':'field__input', 'placeholder':'1500'}),
            'link' : forms.TextInput(attrs={'class':'field__input', 'placeholder':'https://vk.com/qwejid'}),
            'description' : forms.Textarea(attrs={'class':'field__input auto-resize-textarea', 'placeholder':'Стол в хорошем состоянии ...'}),
            
        }
