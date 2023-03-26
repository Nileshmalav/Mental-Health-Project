from django.db import models
from Authentication.models import Person
from datetime import datetime
# Create your models here.


class Topic(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    sno=models.AutoField(default=0, primary_key=True)
    user=models.ForeignKey(Person, on_delete=models.CASCADE,null=True)
    
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE,null=True)
    
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    time_stamp=models.DateTimeField(default=datetime.now())
    

    def __str__(self):
        return self.title


class Likes(models.Model):
    sno=models.AutoField(default=0,primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(default=datetime.now())
    
    
    def __str__(self):
        return self.user.username + " " + self.post.title
    
class Comment(models.Model):
    sno=models.AutoField(default=0,primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    text=models.TextField()
    time_stamp=models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.user.username + " " + self.post.title