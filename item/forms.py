from django import forms
from django.forms import ModelForm
from .models import Category,Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        ordering =('name',)
        verbose_name_plural = 'Categories'
        fields = '__all__'

class NewIteamForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)
        
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
             'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
              'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
               'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
                'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }