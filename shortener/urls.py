from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
    path('delete/<int:pk>/', views.delete_url, name='delete_url'),
]

