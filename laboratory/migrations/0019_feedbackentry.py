# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0018_auto_20161223_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('explanation', models.TextField(blank=True)),
                ('related_file', models.FileField(blank=True, upload_to='media/feedback_entries/')),
            ],
            options={
                'verbose_name_plural': 'Feedback entries',
                'verbose_name': 'Feedback entry',
            },
        ),
    ]
