# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-18 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0018_auto_20190423_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictogram',
            name='warning_word',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sga.WarningWord'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='warningclass',
            name='level',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
        migrations.AlterField(
            model_name='warningclass',
            name='lft',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
        migrations.AlterField(
            model_name='warningclass',
            name='rght',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]