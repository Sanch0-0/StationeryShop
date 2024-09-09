# Generated by Django 5.0.7 on 2024-09-09 10:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favourite', '0001_initial'),
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favouriteproduct',
            name='favourite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_items', to='favourite.favourite'),
        ),
        migrations.AddField(
            model_name='favouriteproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='products',
            field=models.ManyToManyField(through='favourite.FavouriteProduct', to='shop.product'),
        ),
    ]
