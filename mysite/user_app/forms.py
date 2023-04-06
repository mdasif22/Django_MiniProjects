from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class customRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','phone','password1','password2']
