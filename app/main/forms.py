from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    
    class Meta:
        model = News
        fields = ['title', 'text', 'cat', 'image']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'field__input', 'placeholder':'Монополия'}),
            'text' : forms.Textarea(attrs={'class':'field__input auto-resize-textarea', 'placeholder':'Сегодня собираемся для игры в ...'}),
            
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 200:
                raise forms.ValidationError('Длина превышает 200 символов')
            return title
        
