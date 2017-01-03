# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 12:32
from __future__ import unicode_literals

import cashup.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashup', '0002_tillclosure'),
    ]

    operations = [
        migrations.AddField(
            model_name='tillclosure',
            name='coin_10p',
            field=cashup.models.DenominationCountField(default=0, pence_value=10, verbose_name='10p coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='coin_1GBP',
            field=cashup.models.DenominationCountField(default=0, pence_value=100, verbose_name='£1 coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='coin_1p',
            field=cashup.models.DenominationCountField(default=0, pence_value=1, verbose_name='1p coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='coin_20p',
            field=cashup.models.DenominationCountField(default=0, pence_value=20, verbose_name='20p coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='coin_2GBP',
            field=cashup.models.DenominationCountField(default=0, pence_value=200, verbose_name='£2 coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='coin_2p',
            field=cashup.models.DenominationCountField(default=0, pence_value=2, verbose_name='2p coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='coin_50p',
            field=cashup.models.DenominationCountField(default=0, pence_value=50, verbose_name='50p coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='coin_5p',
            field=cashup.models.DenominationCountField(default=0, pence_value=5, verbose_name='5p coins'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='note_10GBP',
            field=cashup.models.DenominationCountField(default=0, pence_value=1000, verbose_name='£10 notes'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='note_20GBP',
            field=cashup.models.DenominationCountField(default=0, pence_value=2000, verbose_name='£20 notes'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='note_5GBP',
            field=cashup.models.DenominationCountField(default=0, pence_value=500, verbose_name='£5 notes'),
        ),
        migrations.AddField(
            model_name='tillclosure',
            name='till_float',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tillclosure',
            name='note_50GBP',
            field=cashup.models.DenominationCountField(default=0, pence_value=5000, verbose_name='£50 notes'),
        ),
        migrations.AlterField(
            model_name='tillclosure',
            name='total_takings',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=12),
        ),
    ]
