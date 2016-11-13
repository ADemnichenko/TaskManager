# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TskMng', '0002_auto_20161106_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_in_process',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_open',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]