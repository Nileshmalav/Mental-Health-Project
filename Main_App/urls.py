from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='main_home'),
    path('location/', views.location, name='location'),
    
    
]