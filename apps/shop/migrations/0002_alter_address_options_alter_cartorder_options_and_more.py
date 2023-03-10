# Generated by Django 4.1.7 on 2023-02-20 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': '1 Адрес', 'verbose_name_plural': '1 Адреса'},
        ),
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name': '2 Заказ в корзину', 'verbose_name_plural': '2 Заказы на корзинe'},
        ),
        migrations.AlterModelOptions(
            name='cartorderitems',
            options={'verbose_name': '3 Заказ в корзине', 'verbose_name_plural': '3 Заказы в корзине'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '4 Категория', 'verbose_name_plural': '4 Категории'},
        ),
        migrations.AlterModelOptions(
            name='poductrevie',
            options={'verbose_name': '5 Отзыв', 'verbose_name_plural': '5 Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '7 Продукт', 'verbose_name_plural': '7 Продукты'},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name': '8 Продавец', 'verbose_name_plural': '8 Поставщики'},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': '9 Жилание', 'verbose_name_plural': '9 Список жиланий'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='tegs',
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.vendor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'Черновик'), ('disabled', 'Отключенный'), ('rejected', 'Отклоненный'), ('in_review', 'На рассмотрении'), ('published', 'Опубликованный')], default='in_review', max_length=10),
        ),
    ]
