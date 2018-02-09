# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 17:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_testscore_itime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
