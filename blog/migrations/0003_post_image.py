# Generated by Django 3.2.23 on 2024-02-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240219_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='media/post/'),
        ),
    ]