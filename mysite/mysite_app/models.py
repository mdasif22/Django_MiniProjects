from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    manage = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    
    def __str__(self):
        return self.task +"- "+str(self.done)
    
    
class Info(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.IntegerField()
    male = models.BooleanField()
    
    def __str__(self):
        return self.name +" - "+str(self.phone)+" - "+str(self.male)



    
    
    
    
    