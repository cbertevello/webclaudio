# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-06-16 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0007_auto_20190616_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='remedio',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
