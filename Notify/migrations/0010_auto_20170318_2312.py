# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 23:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Notify', '0009_auto_20170318_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 18, 23, 12, 53, 779787, tzinfo=utc)),
        ),
    ]
