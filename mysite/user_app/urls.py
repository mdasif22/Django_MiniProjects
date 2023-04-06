from django.urls import path
from user_app import views
#django default login system
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('register',views.register,name='register'),
    #django default login system
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
]
