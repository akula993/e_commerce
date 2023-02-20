from django.db import models
from django.utils.safestring import mark_safe
# from shortuuidfield import ShortUUIDField
from shortuuid.django_fields import ShortUUIDField

from apps.userauths.models import User

STATUS_CHOICE = (
    ('process', 'Процесс'),
    ('shipped', 'Отправленный'),
    ('delivered', 'доставлен'),
)
STATUS = (
    ('draft', 'Черновик'),
    ('disabled', 'Отключенный'),
    ('rejected', 'Отклоненный'),
    ('in_review', 'На рассмотрении'),
    ('published', 'Опубликованный'),
)
RATING = (
    ('1', '★☆☆☆☆'),
    ('2', '★★☆☆☆'),
    ('3', '★★★☆☆'),
    ('4', '★★★★☆'),
    ('5', '★★★★★'),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet='abcdefgh12345')
    title = models.CharField(max_length=150, default='Еда')
    image = models.ImageField(upload_to='category', default='category.jpg')

    class Meta:
        verbose_name = '4 Категория'
        verbose_name_plural = '4 Категории'

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

    def __str__(self):
        return self.title


class Tegs(models.Model):
    pass


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="ven", alphabet='abcdefgh12345')

    title = models.CharField(max_length=150, default="Nestify")
    image = models.ImageField(upload_to=user_directory_path, default='vendor.jpg')
    description = models.TextField(null=True, blank=True, default="Я лутший поставшик!!!")

    address = models.CharField(max_length=100, default='123 main street.')
    contact = models.CharField(max_length=100, default='+7 (915) 472 83 11')
    chat_resp_time = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100, default='100')
    authentic_rating = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = '8 Продавец'
        verbose_name_plural = '8 Поставщики'

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=30, alphabet='abcdefgh12345')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category', verbose_name='Категория')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name='vendor', verbose_name='Поставщик')

    title = models.CharField(max_length=150, default="Свежая груша")
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = models.TextField(null=True, blank=True, default="Этот продукт")

    price = models.DecimalField(max_digits=999999, decimal_places=2, default='1.99')
    old_price = models.DecimalField(max_digits=999999, decimal_places=2, default='2.99')

    specifications = models.TextField(null=True, blank=True)
    # tegs = models.ForeignKey(Tegs, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review')

    status = models.BooleanField(default=True, verbose_name='Статус')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    featured = models.BooleanField(default=False,verbose_name='Рекомендуемые')
    digital = models.BooleanField(default=False, verbose_name='Цифровой')

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet='1234567890')

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    update = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = '7 Продукт'
        verbose_name_plural = '7 Продукты'

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

    def __str__(self):
        return self.title

# Подсчет процентов на сайте {{ p.get_percentage|floatformat:0 }}%
    def get_percentage(self):
       new_price = (self.price / self.old_price) * 100
       return new_price

class ProductImage(models.Model):
    images = models.ImageField(upload_to='product-image', default='product.jpg')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'


""" """



class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=99999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default='process')

    class Meta:
        verbose_name = '2 Заказ в корзину'
        verbose_name_plural = '2 Заказы на корзинe'



class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_on = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200,)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    """quantity"""
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999, decimal_places=2, default='1.99')
    total = models.DecimalField(max_digits=999999, decimal_places=2, default='1.99')

    class Meta:
        verbose_name = '3 Заказ в корзине'
        verbose_name_plural = '3 Заказы в корзине'

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50">' % (self.image))
#########""""Обзор продукта""" Аддрес

class PoductRevie(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product,  on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '5 Отзыв'
        verbose_name_plural = '5 Отзывы'


    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product,  on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '9 Жилание'
        verbose_name_plural = '9 Список жиланий'


    def __str__(self):
        return self.product.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '1 Адрес'
        verbose_name_plural = '1 Адреса'

    # def __str__(self):
    #     return
