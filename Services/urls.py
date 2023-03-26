from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='services_home'),
    path('<str:name>', views.service_type, name='service_type'),
]