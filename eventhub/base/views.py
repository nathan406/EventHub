from django.shortcuts import render
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import UserCreationForm , SignInForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request ,'base/index.html')

def register(request):
    page = 'register'
    form = UserCreationForm()
    
    #user = User

    context = {
        'form':form,
        'page':page,
        #'user':user
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.username = User.username.lower()
            User.save()
            login(request,User)
            
            return redirect('home')
        
        else:
             messages.error(request,"passwords must match")
             messages.error(request,"password must contain small and capital letter special character and digit/s")
             messages.error(request,"username must not be in password ")
             messages.error(request,"try another username and/or password")
             
    
    return render(request,'base/sign.html',context)

def loginUser(request):
    form = SignInForm()

    if request.user.is_authenticated :
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
  
    context ={
        'form':form,
        # 'messages':messages
    }

    return render(request,'base/sign.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'base/home.html')