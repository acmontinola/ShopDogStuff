# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphome', '0006_auto_20161011_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]