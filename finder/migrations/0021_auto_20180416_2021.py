# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0020_auto_20180416_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Genre1',
            field=models.CharField(choices=[('action', 'action'), ('animation', 'animation'), ('crime', 'crime'), ('horror', 'horror'), ('sci-fi', 'sci-fi')], default='Action', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Genre2',
            field=models.CharField(choices=[('action', 'action'), ('animation', 'animation'), ('crime', 'crime'), ('horror', 'horror'), ('sci-fi', 'sci-fi')], default='Romance', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Genre3',
            field=models.CharField(choices=[('action', 'action'), ('animation', 'animation'), ('crime', 'crime'), ('horror', 'horror'), ('sci-fi', 'sci-fi')], default='Thriller', max_length=20),
        ),
    ]
