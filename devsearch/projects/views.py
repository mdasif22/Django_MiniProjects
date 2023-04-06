from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Tag
from .forms import ProjectForm
from django.db.models import Q

def projects(request):
    search_query = ''
    
    if request.GET.get('search_query'):
         search_query = request.GET.get('search_query')
         
    tags = Tag.objects.filter(name__icontains = search_query)
     
    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query) | 
        Q(disc__icontains = search_query) | 
        Q(owner__name__icontains = search_query) | 
        Q(tags__in = tags) )
    
    #projects = Project.objects.all()
    context = {'projects':projects,'search_query' : search_query} 
    return  render(request,'projects/projects.html',context)

def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    #tags = projectobj.tags.all()
    return render(request,'projects/single-project.html',{'project':projectobj})

@login_required(login_url="login")
def create(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url="login")
def update(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url="login")
def delete(request,pk):
    project = Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    
    
    context = {'object' : project}
    return render(request, 'projects/delete_obj.html',context)

