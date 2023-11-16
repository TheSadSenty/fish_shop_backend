from django.db import models
from products.models import Category, Products

class Cart(models.Model):
    item = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #category = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.item,
                                          self.quantity,
                                          self.created_at,
                                          self.updated_at)

    def save(self, *args, **kwargs):
        # Переопределяем метод save для автоматического присвоения категории от продукта
        if self.item:
            self.category = self.item.category

        super().save(*args, **kwargs)