# Generated by Django 4.2.6 on 2023-11-21 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cart_category_alter_cart_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category',
        ),
    ]
