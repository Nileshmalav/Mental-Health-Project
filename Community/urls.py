from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="community_home"),
    path('topic/<str:topic>', views.topic_posts,name="community_topic"),
    path('posts/<int:sno>', views.post,name="community_post"),
    
    path('posts/create', views.create_post,name="community_post_create"),
    path('posts/<int:sno>/comments/create', views.create_comment,name="community_comment"),
    path('posts/<int:sno>/like/', views.post_like,name="community_post_like"),
]