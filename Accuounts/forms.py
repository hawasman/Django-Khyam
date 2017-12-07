from django import forms
from .models import users

class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=15)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = users
        fields = (
            'full_name',
            'username',
            'email',
            'password',
            )
