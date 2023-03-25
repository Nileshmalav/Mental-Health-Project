from django.urls import path
from . import views

urlpatterns = [
   
    path('signup/', views.signup, name='authentication_signup'),
    path('signin/', views.signin, name='authentication_signin'),
    path('signout/', views.signout, name='authentication_signout'),
    
]