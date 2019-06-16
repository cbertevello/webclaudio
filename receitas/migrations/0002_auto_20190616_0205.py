# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-06-16 05:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescricao',
            old_name='data_emissao',
            new_name='data_mes_texto',
        ),
        migrations.RemoveField(
            model_name='remedio',
            name='prescricao',
        ),
        migrations.AddField(
            model_name='prescricao',
            name='data_ano_mes_dia',
            field=models.CharField(default=datetime.datetime(2019, 6, 16, 5, 5, 44, 775878, tzinfo=utc), max_length=8),
            preserve_default=False,
        ),
    ]