# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0005_auto_20171127_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdescription',
            name='Additional_Information',
            field=models.CharField(max_length=100, null=True),
        ),
    ]