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


class UserReview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь")
    user_public_name = models.CharField(
        verbose_name="Публичное имя пользователя", default="Анонимный пользователь")
    text = models.CharField(verbose_name="Отзыв")
    product = models.ForeignKey(
        Products, on_delete=models.SET_NULL, verbose_name="Продукт", null=True)
    is_anonymous = models.BooleanField(
        verbose_name="Анонимный отзыв", default=True)
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.is_anonymous == False:
            self.user_public_name = self.user.last_name+" "+self.user.first_name
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
