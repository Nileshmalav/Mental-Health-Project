from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="talking_buddy_home"),
    path('getresponse/', views.getresponse,name="talking_buddy_get_response"),
]