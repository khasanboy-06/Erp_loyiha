from django import forms
from .models import Homework

class HomeworkForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea())
    homework_file = forms.FileField(widget=forms.FileInput())
