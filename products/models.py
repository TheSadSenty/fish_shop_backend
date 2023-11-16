from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ("name",)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание', blank=True)
    photo = models.ImageField('Изображение', upload_to="products_photos/")
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
