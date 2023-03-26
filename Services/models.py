from django.db import models
from Authentication.models import Person
from datetime import datetime
# Create your models here.
# Create your models here.


class ServiceType(models.Model):
    name=models.CharField(max_length=50, default="none")
    reference=models.CharField(max_length=50, default="none")
    description=models.CharField(max_length=100, default="none")
    
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50, default="")
    expert = models.ForeignKey(Person, on_delete=models.CASCADE)
    service_type=models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    description=models.CharField(max_length=100, default="")
    
    distance=models.IntegerField(null=True,default=0)
    latitude_x=models.FloatField(null=True,default=0)
    longitude_y=models.FloatField(null=True,default=0)

    def __str__(self):
        return self.name

