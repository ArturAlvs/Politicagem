# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_auto_20160909_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatura',
            name='como_foi_eleito',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='candidatura',
            name='eleito',
            field=models.BooleanField(default=False),
        ),
    ]
