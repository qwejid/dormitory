from django.urls import path, include
from . import views

app_name = 'main' 

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('news/<int:news_id>', views.show_news, name='show_news'),
    path('news/category/<int:cat_id>', views.show_category, name='show_category'),
    path('store', views.store, name='store'),
    path('store/<int:card_id>', views.show_card, name='show_card'),
    path('store/category/<int:cat_id>', views.show_prod_category, name='show_prod_category'),
    path('news/add', views.add, name='add'),
    path('store/create_product', views.create_product, name='create_product'),   
]