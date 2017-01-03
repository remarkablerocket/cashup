# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashup', '0003_auto_20170102_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='tillclosure',
            name='till_difference',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='till_total',
            field=models.DecimalField(decimal_places=2, default=1, editable=False, max_digits=12),
            preserve_default=False,
        ),
    ]
