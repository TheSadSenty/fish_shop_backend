# Generated by Django 4.2.6 on 2023-11-18 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_discount_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='to_datetime',
            new_name='duration',
        ),
    ]
