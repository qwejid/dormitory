from django.urls import path
from sberbank import views

urlpatterns = [
    path('payment/callback/', views.callback),
    path('payment/success/', views.redirect, {'kind': 'success'}),
    path('payment/fail/', views.redirect, {'kind': 'fail'}),
    path('payment/status/<str:uid>/', views.StatusView.as_view()),
    path('payment/bindings/<str:client_id>/', views.BindingsView.as_view()),
    path('payment/binding/<str:binding_id>/', views.BindingView.as_view()),
    path('payment/history/<str:client_id>/', views.GetHistoryView.as_view()),
]
