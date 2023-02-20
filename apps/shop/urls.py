from django.urls import path

from apps.shop.views import index, category_list_view, product_list, category_product_list_view

apps_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product-list'),
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>/', category_product_list_view, name='category-product-list'),
]

