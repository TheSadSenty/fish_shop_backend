# Generated by Django 4.2.6 on 2023-11-21 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
