# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 12:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0019_auto_20170311_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apt_test',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 12, 12, 50, 24, 388675), verbose_name='test end time '),
        ),
    ]
