from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', UserLogout, name='logout'),
    path('api/list/', UserListApiView.as_view(), name='ListApi'),
    path('api/retrieve/<int:pk>', UserRetrieveApiView.as_view(), name='RetrieveApi'),
]
