from django import forms 
from mysite_app.models import TaskList
from mysite_app.models import Info

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task','done']
        
        


class InsertInfo(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name','address','phone','male']
                


        
        
        