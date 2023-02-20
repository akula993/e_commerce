from django.contrib import admin

from apps.shop.models import Category, Vendor, Product, ProductImage, CartOrder, CartOrderItems, PoductRevie, \
    Wishlist, Address


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('title', 'category_image',)


@admin.register(Vendor)
class AdminVendor(admin.ModelAdmin):
    list_display = ('title', 'vendor_image',)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    list_display = ('user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status')
    list_editable = ('featured', 'product_status')

# @admin.register(ProductImage)
# class AdminProductImage(admin.ModelAdmin):
#     pass


@admin.register(CartOrder)
class AdminCartOrder(admin.ModelAdmin):
    list_display = ('user', 'price', 'paid_status', 'order_date', 'product_status')


@admin.register(CartOrderItems)
class AdminCartOrderItems(admin.ModelAdmin):
    list_display = ('order', 'invoice_on', 'product_status', 'image', 'qty', 'price', 'total',)


@admin.register(PoductRevie)
class AdminPoductRevie(admin.ModelAdmin):
    list_display = ('user', 'product', 'review', 'rating', 'date')


@admin.register(Wishlist)
class AdminWishlist(admin.ModelAdmin):
    list_display = ('user', 'product', 'date')


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('user', 'address', 'status')
