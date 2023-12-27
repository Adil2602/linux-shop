from django import forms
from .models import Farmer, User
from django.contrib.auth.forms import UserCreationForm

# регистрация пользователя
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

# вход пользователя
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

# регистрация фермера
class FarmerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['phone', 'first_name', 'last_name', 'farm_address', 'card_number', 'card_holder_name', 'expiration_date', 'cvv_code']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['expiration_date'].widget = forms.SelectDateWidget(years=range(2023, 2030))



