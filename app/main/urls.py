from django.urls import path, include
from . import views

app_name = 'main' 

urlpatterns = [
    path('', views.index, name='index'),

    path('news', views.news, name='news'),
    path('news/<int:news_id>', views.show_news, name='show_news'),
    path('news/category/<int:cat_id>', views.show_category, name='show_category'),
    path('news/<int:news_id>/update', views.update_news, name='update_news'),
    path('news/<int:news_id>/delete', views.delete_news, name='delete_news'),
    path('news/add', views.add, name='add'),

    path('store', views.store, name='store'),
    path('store/<int:card_id>', views.show_card, name='show_card'),
    path('store/category/<int:cat_id>', views.show_prod_category, name='show_prod_category'),
    path('store/<int:card_id>/update', views.update_prod, name='update_prod'),
    path('store/<int:card_id>/delete', views.delete_prod, name='delete_prod'),   
    path('store/create_product', views.create_product, name='create_product'),  

    
]