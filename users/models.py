from django.db import models
from products.models import Products
from django.contrib.auth.models import User


class FavoriteProduct(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, verbose_name="Продукт")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Любимый продукт'
        verbose_name_plural = 'Любимые продукты'
