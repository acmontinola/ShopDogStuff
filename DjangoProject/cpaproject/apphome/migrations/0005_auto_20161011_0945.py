# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apphome', '0004_product_clothes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Clothes',
            new_name='Clothes',
        ),
    ]
