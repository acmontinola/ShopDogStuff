# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphome', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
