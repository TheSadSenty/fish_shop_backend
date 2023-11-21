from django.db import models
from products.models import Products


class Cart(models.Model):
    item = models.ForeignKey(
        Products, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.item,
                                          self.quantity,
                                          self.created_at,
                                          self.updated_at)

    class Meta:
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзины пользователей'
