from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_views, name='products'),
    path('product/', views.product_detail, name='product_detail')

]
