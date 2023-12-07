from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'mylogin/index.html')

def userpage(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("mylogin:signup"))
    
    return render(request,"mylogin/userpage.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('mylogin:userpage'))
        else:
            render(request,'mylogin/signup.html')

    return render(request,'mylogin/signin.html',{
        "error":"no authenticated user",
    })

def signup(request):
    return render(request,'mylogin/signup.html')

def logout_views(request):
    logout(request)
    return render(request,'mylogin/index.html',{
        "mes":"was logged out",
    })