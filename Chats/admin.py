from django.contrib import admin

from Chats.models import Message,Chat_Thread,Rooms

admin.site.register(Chat_Thread)
admin.site.register(Message)
admin.site.register(Rooms)