# Generated by Django 3.2.8 on 2021-12-15 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_auto_20211215_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50), max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Slug'),
        ),
    ]
