from django.db import models
from datetime import timedelta


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ("name",)


class Products(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание', blank=True)
    photo = models.ImageField('Изображение', upload_to="products_photos/")
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    category = models.ForeignKey(
        'Category', verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    amount = models.PositiveIntegerField(
        'Количество товара в наличии', blank=False, default=1)
    purchase_quantity = models.PositiveIntegerField(
        'Продано единиц товара', blank=False, default=0)

    addition_datetime = models.DateTimeField(
        'Дата и время добавления товара', editable=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
