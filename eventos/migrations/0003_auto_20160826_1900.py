# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20160826_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='lugar',
            field=models.CharField(max_length=50),
        ),
    ]
