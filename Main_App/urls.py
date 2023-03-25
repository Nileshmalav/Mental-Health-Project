from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='main_home'),
    path('sample/', views.sample, name='main_sample'),
    
    
]