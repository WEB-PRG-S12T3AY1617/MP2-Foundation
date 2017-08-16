from django import forms
from Profile.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'user_name':forms.TextInput(attrs={'class': 'form-control'}),
            'user_username':forms.TextInput(attrs={'class': 'form-control'}),
            'user_password':forms.PasswordInput(attrs={'class': 'form-control'}),
            'user_officefk':forms.Select(attrs={'class': 'form-control'}),
            'user_degreefk':forms.Select(attrs={'class': 'form-control'}),
            'user_occupation':forms.TextInput(attrs={'class': 'form-control'}),
        }
    