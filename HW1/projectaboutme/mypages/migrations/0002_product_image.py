# Generated by Django 4.2.6 on 2024-02-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
