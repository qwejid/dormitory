from django.contrib import admin
from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'author')  # Отображение полей в списке записей
    list_filter = ('date',)  # Добавление фильтрации по полю 'date'
    search_fields = ('title', 'text')  # Поиск по полям 'title' и 'text'


@admin.register(Category)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Category_prod)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'publication_date', 'cat_prod', 'author')


    

