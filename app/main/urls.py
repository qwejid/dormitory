from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('news/<int:news_id>', views.show_news, name='show_news'),
    path('news/category/<int:cat_id>', views.show_category, name='show_category'),
    path('store', views.store, name='store'),
    path('store/<int:card_id>', views.show_card, name='show_card'),
    path('store/category/<int:cat_id>', views.show_prod_category, name='show_prod_category'),
    path('profile', views.profile, name='profile'),
    path('log', views.log, name='log'),
    path('reg', views.reg, name='reg'),
    path('add', views.add, name='add'),
    
    
    
]