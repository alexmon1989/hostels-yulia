# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_googleanalyticscode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(verbose_name='Код HTML')),
            ],
            options={
                'verbose_name': 'Контактные данные в шапке сайта (HTML)',
                'verbose_name_plural': 'Контактные данные в шапке сайта (HTML)',
            },
        ),
    ]
