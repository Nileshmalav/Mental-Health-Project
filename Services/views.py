from django.shortcuts import render
from .models import Service, ServiceType
from Authentication.models import Person
import geopy.distance
# Create your views here.
def home(request):
    person=Person.objects.get(username=request.user)
    service_types=ServiceType.objects.all()
    print(service_types)
    context={
        'services':service_types,
        'person':person
    }
    return render(request, 'Services/service_type.html', context)
    
    
    
    
def service_type(request, name):
    service_type=ServiceType.objects.get(reference=name)
    services=Service.objects.filter(service_type=service_type)
    person=Person.objects.get(username=request.user)
    print(services)
    for service in services:
        person1=Person.objects.get(username=service.expert.username)
        x=person1.latitute_x
        y=person1.longitude_y
        
        coordinate1=(person.latitute_x,person.longitude_y)
        
        coordinate2=(x,y)
        service.distance=int(geopy.distance.geodesic(coordinate1,coordinate2).km)
        
    
    services = sorted(services, key=lambda d: d.distance)
    print(services)
    context={"person":person,"services":services,"service_type":name}
    return render(request, 'Services/home.html',context)