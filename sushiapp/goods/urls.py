from django.contrib import admin
from django.urls import path

from .views import CategoryListAPIView, GoodListAPIView, GoodDetailAPIView

app_name = 'goods'

urlpatterns = [
    path('category/all', CategoryListAPIView.as_view(), name='categories_list'),
    path('product/all', GoodListAPIView.as_view(), name='goods_list'),
    path('product/<int:id>', GoodDetailAPIView.as_view(), name='goods_detail')
    # path('product/<slug:slug>', GoodDetailAPIView.as_view(), name='goods_detail')
]   
