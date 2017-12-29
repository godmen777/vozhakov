from products.models import Product, Category
from django.shortcuts import render


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {
        'products': products
    })