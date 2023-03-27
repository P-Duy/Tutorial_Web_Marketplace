from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm


urlpatterns = [
    
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('login/',auth_views.LoginView.as_view(template_name='base/login.html',authentication_form=LoginForm),name='login'),
    path('signup/',views.signup,name='signup'),
]