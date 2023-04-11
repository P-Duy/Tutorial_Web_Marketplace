from django import forms
from django.forms import ModelForm
from .models import Conversation,ConversationMessage

class ConversationMessageFrom(forms.ModelForm):
    class Meta:
        model= ConversationMessage
        fields = ('content',)
        widgets={
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
                })
        }