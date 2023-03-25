from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models
from Authentication.models import Person



class Chat_Thread(models.Model):
    sno=models.AutoField(primary_key=True,auto_created = True,serialize=True,default=None)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='receiver')
    last_message=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.sender.username + " to  " + self.receiver.username
    

class Rooms(models.Model):
    sno=models.AutoField(primary_key=True,auto_created = True,serialize=True,default=None)
    name=models.CharField(max_length=100)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='room_sender')
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='room_receiver')
    def __str__(self):
        return self.sender.username + " to  " + self.receiver.username
    
    


class Message(models.Model):
    sno=models.AutoField(primary_key=True,auto_created = True,serialize=True,default=None)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='received_messages',default=None)
    
    content = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.sender.username + " to " + self.receiver.username
