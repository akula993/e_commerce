from django.urls import path

from apps.shop.views import index

apps_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
]
