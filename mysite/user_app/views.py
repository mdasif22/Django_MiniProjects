from django.shortcuts import render,redirect
from .forms import customRegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = customRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Is Created!! Login to get started!!"))
            return redirect('login')
    else:
        register_form = customRegistrationForm()
    return render(request,'register.html',{'register_form':register_form})