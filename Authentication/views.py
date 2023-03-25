
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Authentication.models import Person


#signin
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('main_home')
        return redirect('authentication_signin')
    return render(request, 'authentication/index.html')


#signup
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        name=request.POST['name']
        password=request.POST['password']
        myperson=Person(name=name, email=email,username=username)
        myuser=User.objects.create_user(username, email, password)
        myuser.first_name=name
        myuser.last_name=""
        myperson.save()
        myuser.save()
        
        
        return redirect('authentication_signin')
    return render(request, 'authentication/index.html')


#signout
def signout(request):
    logout(request)
    return redirect("main_home")




