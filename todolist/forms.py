from django import forms
from django.forms import Form
from .models import List

class Listview(forms.ModelForm):
    class Meta:
        model=List
        fields=['item','completed']