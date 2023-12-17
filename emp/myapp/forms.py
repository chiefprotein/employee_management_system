from django.forms import ModelForm, Textarea
from django.forms.widgets import Widget
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(ModelForm):
    class Meta:
        model = emp
        fields = '__all__'

        widgets = {
            'dateb' : DateInput(),
            'datej' : DateInput(),
        }

