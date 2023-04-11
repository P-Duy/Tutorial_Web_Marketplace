from django.urls import path

from . import views


app_name = 'conversations'

urlpatterns = [
    path('new/', views.new,name='new'),
]
