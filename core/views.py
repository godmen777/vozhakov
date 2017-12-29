from django.shortcuts import render
from products.models import Product, Category


def index_view(request):

    products = Product.objects.all()

    return render(request, "core/home.html", {
        'name': 'Home page',
        'products': products,
    })
