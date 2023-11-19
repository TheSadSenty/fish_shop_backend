# Generated by Django 4.2.6 on 2023-11-15 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_purchase_quantity_alter_products_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveIntegerField(default=0, verbose_name='Процент')),
                ('from_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время начала действия скидки')),
                ('to_datetime', models.DurationField(default=datetime.timedelta(days=7), verbose_name='Дата и время окончания действия скидки')),
            ],
        ),
    ]