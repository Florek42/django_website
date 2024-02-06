from django.urls import path
from . import views

#url configs

urlpatterns = [
    path('home/', views.MainApp),
    
]