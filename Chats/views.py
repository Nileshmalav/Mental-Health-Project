from django.shortcuts import render, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import  Message,Chat_Thread,Rooms
from Authentication.models import Person
from datetime import datetime



@login_required
def index(request):
    person=Person.objects.get(username=request.user)
    thread=Chat_Thread.objects.filter(sender=person) |  Chat_Thread.objects.filter(receiver=person)
    thread=thread.all().order_by('-last_message')
    experts=Person.objects.filter(type="expert")
    context = {"user":person,"threads":thread,"experts":experts}
    return render(request, "chats/index.html",context=context)


@login_required
def send(request):
    
    if request.method == "POST":
        sender=request.POST['sender']
        receiver=request.POST['receiver']
        message=request.POST['message']
        receiver=Person.objects.get(username=receiver)
        sender=Person.objects.get(username=sender)
        
        
        mymesage=Message(sender=sender,receiver=receiver,content=message)
        mythread=(Chat_Thread.objects.filter(sender=sender,receiver=receiver) |  Chat_Thread.objects.filter(receiver=sender,sender=receiver)).first()
        
        if mythread:
            mythread.last_message=datetime.now()
        else:
            mythread=Chat_Thread(sender=sender,receiver=receiver,last_message=datetime.now())
        mythread.save()
        mymesage.save()
        return HttpResponse("success")
    
        
        

@login_required
def get_chats(request,to_user):
    person=Person.objects.get(username=request.user)
    receiver=Person.objects.get(username=to_user)
    mychats=Message.objects.filter(sender=person,receiver=receiver) | Message.objects.filter(sender=receiver,receiver=person)
    mychats=mychats.all().order_by('-timestamp')
    
    myroom=(Rooms.objects.filter(sender=person,receiver=receiver) | Rooms.objects.filter(sender=receiver,receiver=person)).first()
    
    
    
    if  not myroom:
        myroom=Rooms(sender=person,receiver=receiver,name=person.username+"to"+receiver.username)
        myroom.save()
        
    # myroom=(Rooms.objects.filter(sender=person,receiver=receiver) | Rooms.objects.filter(sender=receiver,receiver=person)).first()
    myroom=myroom
    mythread=(Chat_Thread.objects.filter(sender=person,receiver=receiver) |  Chat_Thread.objects.filter(receiver=person,sender=receiver)).first()
        
    if mythread:
        mythread.last_message=datetime.now()
    else:
        mythread=Chat_Thread(sender=person,receiver=receiver,last_message=datetime.now())
    mythread.save()
    
    myhtml=render(request, "chats/chat.html", {"chats":mychats,"user":person,"room":myroom})
    return JsonResponse({"html":myhtml.content.decode("utf-8"),"room":myroom.name})
    

@login_required
def room(request, room_name):
    person=Person.objects.get(username=request.user)
    receiver=Person.objects.get(username=room_name)
    mychats=Message.objects.filter(sender=person,receiver=receiver) | Message.objects.filter(sender=receiver,receiver=person)
    mychats=mychats.all().order_by('-timestamp')
    context = {"user":person,"room_name": room_name,"receiver":receiver,"chats":mychats}
    return render(request, "chats/chat.html", context=context)




@login_required
def community_chats(request,name):
    person=Person.objects.get(username=request.user)
    context = {"user":person,"room_name": name,"chats":[]}
    return render(request, "chats/community.html", context=context)