from django.shortcuts import render,HttpResponse,redirect
from .models import Topic,Post,Comment,Likes
from Authentication.models import Person
# Create your views here.
def home(request):
    person = Person.objects.get(username=request.user)
    topics = Topic.objects.all()
    
    latest_posts = Post.objects.all().order_by('-time_stamp')[:10]
    
    context={"user":person,"topics":topics,"recommended_posts":latest_posts,"yourfeed":latest_posts}
    return render(request,'community/posts.html',context)


def topic_posts(request,topic):
    person = Person.objects.get(username=request.user)
    
    topics = Topic.objects.all()
    topic_posts = Post.objects.filter(topic__name=topic).order_by('-time_stamp')
    latest_posts = Post.objects.all().order_by('-time_stamp')[:10]
    
    context={"topics":topics,"yourfeed":topic_posts,"recommended_posts":latest_posts,"topics":topics}
    return render(request,'community/posts.html',context)

def post(request,sno):
    person = Person.objects.get(username=request.user.username)
    
    topics = Topic.objects.all()
    post = Post.objects.get(sno=sno)
    comments = Comment.objects.filter(post=post).order_by('-time_stamp')
    latest_posts = Post.objects.all().order_by('-time_stamp')[:10]
    
    context={"topics":topics,"post":post,"comments":comments,"recommended_posts":latest_posts,"topics":topics}
    return render(request,'community/post.html',context)



def create_post(request):
    if request.method=="POST":
        user=request.user
        person=Person.objects.get(username=user.username)
        topic=request.POST["topic"]
        title=request.POST["title"]
        content=request.POST["content"]
        mypost=Post(title=title,content=content,topic=Topic.objects.get(name=topic),user=person)
        mypost.save()
        return redirect("community_home")
    return HttpResponse("404 - Not Found")

def create_comment(request,sno):
    if request.method=="POST":
        user=request.user
        person=Person.objects.get(username=user.username)
        post=Post.objects.get(sno=sno)
        text=request.POST["text"]
        mycomment=Comment(text=text,post=post,user=person)
        mycomment.save()
        return redirect("community_home")
    return HttpResponse("404 - Not Found")


def post_like(request):
    
    return HttpResponse("Success")