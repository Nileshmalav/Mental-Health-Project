from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from Authentication.models import Person
from .models import BuddyMessage

from .gptcode import ask_ai
# Create your views here.
@login_required
def home(request):
    person=Person.objects.get(username=request.user)
    chats=(BuddyMessage.objects.filter(sender=person.username) | BuddyMessage.objects.filter(receiver=person.username)).all().order_by('time_stamp')
    context={"chats":chats,"user":person}
    return render(request,'chats/talkingBuddy.html',context)
    

@login_required
def getresponse(request):
    if request.method=="POST":
        person=Person.objects.get(username=request.user)
        message=request.POST['message']

        myMessage=BuddyMessage(sender=person.username,receiver="buddy",content=message)
        myMessage.save()
        
        response=ask_ai(message)
        buddyMessage=BuddyMessage(sender="buddy",receiver=person.username,content=response)
        buddyMessage.save()
        
        
        
        return JsonResponse({"response":response})
        
        
        
    return HttpResponse("Failed")