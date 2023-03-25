# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="chats_index"),
    path("send/", views.send, name="chats_send"),
    path("to/<str:to_user>/", views.get_chats, name="chats_get_chats"),
    path("get_room/", views.room, name="chats_get_room"),
]