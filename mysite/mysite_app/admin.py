from django.contrib import admin
from mysite_app.models import TaskList,Info
# Register your models here.

#Adding search bar in admin page
class MyTasks(admin.ModelAdmin): 
    search_fields = ['task']

admin.site.register(TaskList,MyTasks)
admin.site.register(Info)





