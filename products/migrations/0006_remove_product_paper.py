# Generated by Django 3.2.23 on 2024-02-06 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20240205_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='paper',
        ),
    ]
