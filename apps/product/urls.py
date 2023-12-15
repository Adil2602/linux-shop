from django.urls import path
from .views import *

urlpatterns = [
    path('product/',
         ProductList.as_view(),
         name='product'),

    path('',
         CategoryList.as_view(),
         name='index'),

    path('category/<int:pk>/products/',
         ProductListByCategory.as_view(),
         name='category_detail'),

    path('api/list/',
         ProductListApiView.as_view(),
         name='ListApi'),

    path('api/retrieve/',
         ProductRetrieveApiView.as_view(),
         name='RetrieveApi'),
]
