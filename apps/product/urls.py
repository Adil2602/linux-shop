from django.urls import path
from .views import *

urlpatterns = [
    path('product/',
         ProductList.as_view(),
         name='product'),

    path('api/list/',
         ProductListApiView.as_view(),
         name='ListApi'),

    path('api/retrieve/',
         ProductRetrieveApiView.as_view(),
         name='RetrieveApi'),
]
