from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite_app.models import TaskList,Info
from mysite_app.forms import TaskForm,InsertInfo
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
 
def test(request):
    if request.method=="POST":
        form = InsertInfo(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New User is added!!"))
        return redirect('test')
    
    else:
        all_obj = Info.objects.all
        #my_dict ={'insert_me' : "Hello i am from views.py !!"}
        return render(request,'mysite_app/index.html',{'all_obj' : all_obj})
        #return render(request,'mysite_app/index.html',context = my_dict)
    # return HttpResponse("Hello Python World!!. View 1")

@login_required
def index1(request):
    if request.method=="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            #user can add new task in db
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request,("New Task is added!!"))
        return redirect('todolist')
        
    else:
        # all_tasks= TaskList.objects.all()
        #showing only that task which belongs to tht particular user
        all_tasks= TaskList.objects.filter(manage=request.user)
        # text = {'welcome_text' : "Welcome to MYSITE"}
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        
        return render(request,'todolist.html',{'all_tasks' : all_tasks})

def index(request):
    text = {'index_text' : "Welcome to  Index Page"}
    return render(request,'index.html',text)

def contact(request):
    text = {'contact_text' : "Welcome to Contact Page"}
    return render(request,'contact.html',text)

def about(request):
    text = {'about_text' : "Welcome to About Us Page"}
    return render(request,'about.html',text)

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("UNAUTHORISED ACCESS!!! YOU CANT ACCESS!!"))
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method=="POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task is edited!!"))
        return redirect('todolist')
    else:
        task_obj= TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj' : task_obj})
     
@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("UNAUTHORISED ACCESS!!! YOU CANT ACCESS!!"))
    return redirect('todolist')
    
@login_required 
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request,("UNAUTHORISED ACCESS!!! YOU CANT ACCESS!!"))
    return redirect('todolist')

