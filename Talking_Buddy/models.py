
# Create your models here.
from django.db import models
from Authentication.models import Person
from datetime import datetime

class BuddyMessage(models.Model):
    sender = models.TextField(default="",null=True)
    receiver=models.TextField(default="Buddy",null=True)
    content = models.TextField()
    
    time_stamp = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.sender+" "+self.receiver+" "+self.content
