from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    name = forms.CharField(label = "Name", max_length = 100)
    
    MY_OCCUPATIONS = (
        ('opt0','Academic'),
        ('opt1','Office'),
    )
    
    occupation_field = forms.ChoiceField(widget=forms.RadioSelect, choices = MY_OCCUPATIONS)
    user_name = forms.CharField(label = "username", max_length = 100)
    password = forms.CharField(label = "password", max_length = 20)
    
    
    