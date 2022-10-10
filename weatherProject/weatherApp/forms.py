from tkinter import Widget
from django.forms import ModelForm, TextInput 
from .models import *
class cityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {'city_name': TextInput(attrs={'class':'form-control', 'placeholdeer':'enter your city'})}