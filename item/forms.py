
from django.forms import ModelForm
from .models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        ordering =('name',)
        verbose_name_plural = 'Categories'
        