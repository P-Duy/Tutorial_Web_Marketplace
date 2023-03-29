from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.new, name = 'new-item'),
    path('item/<str:pk>', views.detail, name='detail'),
]
