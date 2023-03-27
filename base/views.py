from django.shortcuts import render,redirect
from django.http import HttpResponse
from item.models import Item,Category
from .forms import SignupFrom
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    context= {'items': items, 'categories': categories}
    return render(request, 'base/index.html', context)


def contact(request):
    return render(request, 'base/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupFrom()
    
    context ={'form': form}
    return render(request, 'base/signup.html', context)