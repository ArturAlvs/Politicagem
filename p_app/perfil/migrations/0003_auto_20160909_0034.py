# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20160909_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatura',
            name='estado',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='politico',
            name='imagem',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
