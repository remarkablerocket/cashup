# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 21:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashup', '0030_auto_20170108_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outlet',
            name='_staff',
        ),
    ]
