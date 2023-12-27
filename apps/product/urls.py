from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('product', ProductListApiViewSet, basename='product')

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('', CategoryList.as_view(), name='category'),
    path('category/detail/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),

    path('product/', ProductList.as_view(), name='product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('add/', create_product, name='add_product'),

    path('search/', Search.as_view(), name='search'),

]

