from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from rest_framework.viewsets import GenericViewSet

from .forms import RegisterForm, LoginForm, FarmerRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework import viewsets, mixins
from django.template.context_processors import request

from .models import User, Farmer
from .serializers import UserSerializer
from ..product.models import Product


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




@login_required
def my_profile(request):
    current_user = request.user
    user_products = Product.objects.filter(user=current_user)
    is_farmer = current_user.is_farmer
    return render(request, 'profile.html', {'user': current_user, 'user_products': user_products, 'is_farmer': is_farmer})


class FarmerRegistrationView(CreateView):
    model = Farmer
    form_class = FarmerRegistrationForm
    template_name = 'ForS.html'
    success_url = 'profile'

    def post(self, request):
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            farmer = form.save(commit=False)
            farmer.user = request.user
            farmer.save()

            return redirect('profile')

        return render(request, self.template_name, {'form': form})
