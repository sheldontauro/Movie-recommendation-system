# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0011_auto_20180405_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermovies',
            name='c_movie_id',
        ),
        migrations.AddField(
            model_name='usermovies',
            name='c_movie_title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
