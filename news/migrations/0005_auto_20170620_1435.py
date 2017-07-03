# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170620_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='height_field',
            field=models.PositiveIntegerField(default=615),
        ),
        migrations.AddField(
            model_name='news',
            name='width_field',
            field=models.PositiveIntegerField(default=973),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', help_text='Изображение будет автоматически приведено к размеру 973px * 615px', null=True, upload_to='', verbose_name='Изображение', width_field='width_field'),
        ),
    ]
