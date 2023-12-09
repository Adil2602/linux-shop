from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.context_processors import request

# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        password = data['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт заблокирован')
        return HttpResponse('Такого пользователя не существует')

def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
