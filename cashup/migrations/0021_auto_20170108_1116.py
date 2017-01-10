# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 11:16
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Set closed_by to outlet owner - note original data is lost
    TillClosure = apps.get_model('cashup', 'TillClosure')
    for tc in TillClosure.objects.all():
        tc.closed_by = tc.outlet.user
        tc.save()

def reverse_func(apps, schema_editor):
    # Set closed_by to closed_by.username (eg User.username)
    TillClosure = apps.get_model('cashup', 'TillClosure')
    for tc in TillClosure.objects.all():
        tc.closed_by = tc.user.username
        tc.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cashup', '0020_auto_20170108_1115'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
