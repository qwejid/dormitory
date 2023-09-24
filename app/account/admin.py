from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo','room', 'contract_number', 'student_ID', )

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')

# Регистрируем административный класс
admin.site.unregister(User)  # Сначала отключаем стандартный класс User
admin.site.register(User, CustomUserAdmin) 