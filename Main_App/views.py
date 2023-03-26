from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from Authentication.models import Person



#Register 
def home(request):
    if request.user.is_authenticated:  
        return render(request, 'home/index.html')
    else:
        return redirect('authentication_signin')
    
    
    
def location(request):
    person=Person.objects.get(username=request.user)
    print(request.POST)
    person.latitute_x=request.POST['latitude']
    person.longitude_y=request.POST['longitude']
    print(request.POST['longitude'])
    person.save()
    return HttpResponse("success")