from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from rest_framework.viewsets import GenericViewSet

from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework import viewsets, mixins
from django.template.context_processors import request

from .models import User
from .serializers import UserSerializer


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        email = data['email']
        password = data['password1']
        user = authenticate(username=username, email=email,
                            password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('category')
            else:
                return HttpResponse('Ваш аккаунт забанен')
        return HttpResponse('Такого юзера не существует')


def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('category')


# API


class UserApiViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     # mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
