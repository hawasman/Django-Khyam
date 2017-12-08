from django import forms
from .models import users

class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=15)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = users
        fields = (
            'full_name',
            'username',
            'email',
            'password',
            )

class LoginForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['username','password']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'اسم المستخدم','id':'username','aria-describedby':'usernameHelp',}),
            'password' : forms.TextInput(attrs={'class':'form-control','placeholder':'كملة المرور','id':'password','aria-describedby':'passwordHelp',}),
        }
