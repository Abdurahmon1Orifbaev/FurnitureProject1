# Generated by Django 5.0 on 2023-12-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_infomodel_rename_kit_model_kitmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='kitmodel',
            name='image',
        ),
    ]
