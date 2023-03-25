from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect




#Register 
def home(request):
    if request.user.is_authenticated:  
        return render(request, 'home/index.html')
    else:
        return redirect('authentication_signin')
    
    
    
def sample(request):
    return render(request, 'base/base1.html')