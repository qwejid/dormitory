from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account' 

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('log', views.log, name='log'),
    path('reg', views.reg, name='reg'), 
    path('logout_user', views.logout_user, name='logout_user'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
