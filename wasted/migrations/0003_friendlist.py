# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-23 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wasted', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasted.Person')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasted.Person')),
            ],
        ),
    ]