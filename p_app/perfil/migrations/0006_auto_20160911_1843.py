# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0005_auto_20160911_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatura',
            name='partido',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perfil.Partido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='politico',
            name='partido_atual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Partido'),
        ),
    ]
