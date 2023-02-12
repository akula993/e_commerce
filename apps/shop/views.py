from django.shortcuts import render


def index(request):
    return render(request, 'shop/products/index.html')