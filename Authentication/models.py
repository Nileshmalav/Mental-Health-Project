from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50, default="")
    email=models.CharField(max_length=50,null=True)
    img = models.ImageField(upload_to = "static/Profile/",default="None",null=True)
    age = models.IntegerField(null=True)
    gender = models.TextField(choices=(("Male","Male"),( "Female","Female"),),default="None",null=True)
    type=models.TextField(choices=(("user","user"),( "expert","expert"),("service provider","service provider"),("admin","admin")), default="user")
    active=models.BooleanField(default=False)
    
    latitute_x=models.FloatField(null=True,default=0)
    longitude_y=models.FloatField(null=True,default=0)
    
    
    
    last_login = models.DateTimeField(default=datetime.datetime.now)
    last_modified = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.username 

