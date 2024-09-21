# Generated by Django 5.0.7 on 2024-09-11 15:24

import django.db.models.deletion
import django.utils.timezone
import image_cropping.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='image')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '200x200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, verbose_name='price')),
                ('discount', models.SmallIntegerField(blank=True, default=0, verbose_name='discount')),
                ('brand', models.CharField(max_length=20, verbose_name='brand')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_ratings', to='shop.product')),
            ],
        ),
    ]
