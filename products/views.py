from django.shortcuts import render, get_object_or_404
from .models import Product

def products_views(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})



def product_detail(request):
    return render(request, 'products/product_detail.html')

