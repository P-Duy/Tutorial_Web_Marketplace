from django.urls import path
from . import views

urlpatterns = [
    path('item/<str:pk>', views.detail, name='detail'),
]
