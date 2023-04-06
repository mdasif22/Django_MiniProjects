from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .forms import CustomUserCreationForm
from .models import Profiles,Skill

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist!!')
        
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or Password is Invalid!!!')
    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request,'Username Logged Out!!!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,'User Created!!!')
            
            login(request,user)
            return redirect('profiles')
        
        else:
            messages.success(request,'Error has occurred during registration!!')
    context = {'page':page, 'form':form}
    return render(request,'users/login_register.html',context)

def profiles(request):
    search_query = ''
    
    if request.GET.get('search_query'):
         search_query = request.GET.get('search_query')
         
    skills = Skill.objects.filter(name__icontains = search_query)
    
    #profiles = Profiles.objects.all()
    profiles = Profiles.objects.distinct().filter(
        Q(name__icontains = search_query) | Q(short_into__icontains = search_query) | Q(skill__in = skills) )
    
    context = {'profiles':profiles}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profiles.objects.get(id=pk)
    
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    
    context = {'profile':profile,'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request,'users/user-profile.html',context)