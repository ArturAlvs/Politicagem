# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20160909_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='politico',
            old_name='sobre_nome',
            new_name='sobrenome',
        ),
        migrations.RemoveField(
            model_name='doacao',
            name='politico',
        ),
        migrations.AddField(
            model_name='doacao',
            name='candidatura',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perfil.Candidatura'),
            preserve_default=False,
        ),
    ]
