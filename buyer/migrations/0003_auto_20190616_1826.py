# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-17 01:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_auto_20190616_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'verbose_name': 'Buyer', 'verbose_name_plural': 'Buyer Orders'},
        ),
    ]
