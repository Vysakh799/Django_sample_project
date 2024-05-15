from django import forms
from .models import *

class user_form(forms.Form):
    roll=forms.IntegerField()
    name=forms.CharField()
    age=forms.IntegerField()

class model_form(forms.ModelForm):
    class Meta:
        model=student #name of the model
        fields='__all__'  #for connecting all fields
        # fields=['roll','name'] # for connecting specific fields
        widgets={
            'roll':forms.NumberInput(attrs={'class':'form-controller bg-info'})
        }