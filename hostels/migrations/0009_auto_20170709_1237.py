# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0008_auto_20170627_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hostel',
            options={'ordering': ['id'], 'verbose_name': 'Хостел', 'verbose_name_plural': 'Список хостелов'},
        ),
    ]
