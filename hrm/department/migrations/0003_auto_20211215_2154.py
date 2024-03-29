# Generated by Django 3.2.8 on 2021-12-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_auto_20211128_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, verbose_name='Slug'),
        ),
    ]
