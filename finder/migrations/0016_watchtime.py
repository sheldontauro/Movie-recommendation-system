# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0015_usermovies_c_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='watchtime',
            fields=[
                ('w_time', models.IntegerField(default=1, primary_key=True, serialize=False)),
            ],
        ),
    ]
