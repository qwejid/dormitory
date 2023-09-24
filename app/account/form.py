from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileEditForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ('date_of_birth', 'photo', 'room')

class RegisterUserForm(UserCreationForm):
        username = forms.CharField(required=True)
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        password1 = forms.CharField(required=True)
        password2 = forms.CharField(required=True)
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
    

class UserEditForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email')

    