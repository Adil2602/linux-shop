from django.urls import path, include

from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register('user', UserApiViewSet, basename='user')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', UserLogout, name='logout'),
    path('profile/', my_profile, name='profile'),
    path('farmer/', FarmerRegistrationView.as_view(), name='farmer'),
]
