from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django import forms


# Create your views here.

class GetForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Username"
    }))
    username.label = ""
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Password"
    }))
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
            return HttpResponseRedirect(reverse('mylogin:signup'))

    return render(request,'mylogin/signin.html',{
        "error":"no authenticated user",
    })

def signup(request):
    err = ''
    if request.method == "GET":
        form = GetForm(request.GET)
        if form.is_valid():
            usern = form.cleaned_data["username"]
            passw = form.cleaned_data["password"]
            if not User.objects.filter(username=usern).exists():
                newuser = User.objects.create_user(usern,password=passw)
                newuser.save()
                return HttpResponseRedirect(reverse('mylogin:signin'))
            else:
                err = 'this user exist'
                
    return render(request,'mylogin/signup.html',{
        'form':GetForm(),
        'err':err
        
    })

def logout_views(request):
    logout(request)
    return render(request,'mylogin/index.html',{
        "mes":"was logged out",
    })