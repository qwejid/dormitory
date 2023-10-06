from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")  # Поле для хранения названия новости
    image = models.ImageField(upload_to='news_images/%Y/%m/%d', blank=True ,verbose_name="Изображение")  # Поле для хранения картинки (требуется установить библиотеку Pillow)
    text = models.TextField(verbose_name="Текст")  # Поле для хранения текста новости
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)  # Поле для хранения даты новости
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Добавьте поле ForeignKey для автора новости

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('main:show_news', kwargs={'news_id': self.pk})
    
    def get_absolute_update_url(self):
        return reverse('main:update_news', kwargs={'news_id': self.pk})
    
    def get_absolute_delete_url(self):
        return reverse('main:delete_news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новость"

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:show_category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name_plural = "Категории"
        
class Product(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='store_images/%Y/%m/%d', blank=True ,verbose_name="Картинка товара")
    description = models.TextField(verbose_name='Описание')
    cat_prod = models.ForeignKey('Category_prod', on_delete=models.PROTECT, verbose_name="Категория товара")
    price = models.DecimalField(max_digits=10, decimal_places=0,  verbose_name='Цена')
    link = models.URLField(max_length=200, verbose_name='Ссылка')
    publication_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Добавьте поле ForeignKey для автора новости

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:show_card', kwargs={'card_id': self.pk})
    
    def get_absolute_update_url(self):
        return reverse('main:update_prod', kwargs={'card_id': self.pk})
    
    def get_absolute_delete_url(self):
        return reverse('main:delete_prod', kwargs={'card_id': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Category_prod(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Категория товара")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:show_prod_category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name_plural = "Категории товаров"

