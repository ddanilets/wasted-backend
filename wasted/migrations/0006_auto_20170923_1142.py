# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-23 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasted', '0005_trackedactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackedactivity',
            name='endTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='trackedactivity',
            name='startTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
