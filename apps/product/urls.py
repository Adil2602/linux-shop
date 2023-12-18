from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductList.as_view(), name='product'),
    path('', CategoryList.as_view(), name='category'),
    path('category/detail/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('api/list/', ProductListApiView.as_view(), name='ListApi'),
    path('api/retrieve/', ProductRetrieveApiView.as_view(), name='RetrieveApi'),
]

