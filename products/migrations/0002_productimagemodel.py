# Generated by Django 4.2.8 on 2023-12-12 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'product image',
                'verbose_name_plural': 'product images',
            },
        ),
    ]