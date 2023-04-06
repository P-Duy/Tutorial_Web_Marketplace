from django.urls import path
from . import views

app_name ='item'

urlpatterns = [
    path('item/', views.new, name = 'new-item'),
    path('item/<str:pk>', views.detail, name='detail'),
    path('item/edit/<str:pk>', views.edit, name='edit-item'),
    path('item/delete/<str:pk>', views.delete, name='delete-item'),
    
]
