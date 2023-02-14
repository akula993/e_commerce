from django.db import models
from django.utils.safestring import mark_safe
# from shortuuidfield import ShortUUIDField
from shortuuid.django_fields import ShortUUIDField

from apps.userauths.models import User


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet='abcdefgh12345')
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

    def __str__(self):
        return self.title


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="ven", alphabet='abcdefgh12345')

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True)

    address = models.CharField(max_length=100, default='123 main street.')
    contact = models.CharField(max_length=100, default='+7 (915) 472 83 11')
    chat_resp_time = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100, default='100')
    authentic_rating = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
