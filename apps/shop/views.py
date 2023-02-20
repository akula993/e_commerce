from django.db.models import Count
from django.shortcuts import render

from apps.shop.models import Product, Category


def index(request):
    # products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(product_status='published', featured=True, )
    context = {
        'products': products,
    }

    return render(request, 'shop/products/index.html', context)


def product_list(request):
    products = Product.objects.filter(product_status='published', )
    context = {
        'products': products,
    }

    return render(request, 'shop/products/product-list.html', context)


def category_list_view(request):
    categorys = Category.objects.all()
    # categorys = Category.objects.all().annotate(product_count=Count('product'))
    context = {
        'categorys': categorys,
    }
    return render(request, 'shop/products/category-list.html', context)


def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    product = Product.objects.filter(product_status='published', category=category)
    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'shop/products/category-product-list.html', context)