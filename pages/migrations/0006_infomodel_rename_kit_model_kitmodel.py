# Generated by Django 5.0 on 2023-12-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_rename_product_kit_model_kit_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('man', models.CharField(max_length=255)),
                ('work', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'info',
                'verbose_name_plural': 'infoes',
            },
        ),
        migrations.RenameModel(
            old_name='kit_Model',
            new_name='kitModel',
        ),
    ]
