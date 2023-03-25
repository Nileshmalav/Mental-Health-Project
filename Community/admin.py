from django.contrib import admin
from .models import Post, Likes, Comment,Topic
# Register your models here.
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comment)