from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'room', 'contract_number', 'student_ID']

        widgets = {
           'room' : forms.TextInput(attrs={'placeholder':'Введите номер комнаты'}),
           'contract_number' : forms.TextInput(attrs={ 'placeholder':'Введите номер договора о проживании'}),
           'contract_number' : forms.TextInput(attrs={ 'placeholder':'Введите номер студ.билета'}),
           
        }

class RegisterUserForm(UserCreationForm):
        
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)        
        email = forms.EmailField(required=True)

        class Meta:
            model = User
            fields = [
                "username",
                "email",
                "password1",
                "password2",
                "first_name",
                "last_name",
            ]
            labels = {
                "username": "Имя пользователя",
                "last_name": "Фамилия",
                "first_name": "Имя",
                "email": "Email",
                "password1": "Пароль",
                "password2": "Подтверждение пароля",
            }
        def save(self, commit=True):
            user = super(RegisterUserForm, self).save(commit=False)  # Создаем пользователя, но не сохраняем его в БД

            # Устанавливаем значения полей "first_name", "last_name" и "email"
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.email = self.cleaned_data["email"]

            if commit:
                user.save()  # Сохраняем пользователя, если commit=True

            return user
    



    