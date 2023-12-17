from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'zmdi zmdi-account material-icons-name',
        'placeholder': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'zmdi zmdi-email',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'zmdi zmdi-lock',
        'placeholder': 'Your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'zmdi zmdi-lock-outline',
        'placeholder': 'Repeat your password'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'zmdi zmdi-account material-icons-name',
        'placeholder': 'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'zmdi zmdi-account material-icons-name',
        'placeholder': 'Email'
    }))

    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'zmdi zmdi-account material-icons-name',
        'placeholder': 'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'zmdi zmdi-account material-icons-name',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'zmdi zmdi-lock',
        'placeholder': 'Password'
    }))