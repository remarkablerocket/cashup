# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 14:40
from __future__ import unicode_literals

import cashup.models
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='NotesHelpText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(help_text='Enter a shop name or location', max_length=24)),
                ('default_float', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outlets', to='cashup.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnel', to='cashup.Business')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffPositions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager', models.BooleanField(default=False)),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='cashup.Outlet')),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='cashup.Personnel')),
            ],
        ),
        migrations.CreateModel(
            name='TillClosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close_time', models.DateTimeField(default=cashup.models.time)),
                ('cash_takings', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('card_takings', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('total_takings', models.DecimalField(decimal_places=2, editable=False, max_digits=12)),
                ('note_50GBP', cashup.models.DenominationCountField(default=0, pence_value=5000, verbose_name='£50 notes')),
                ('note_20GBP', cashup.models.DenominationCountField(default=0, pence_value=2000, verbose_name='£20 notes')),
                ('note_10GBP', cashup.models.DenominationCountField(default=0, pence_value=1000, verbose_name='£10 notes')),
                ('note_5GBP', cashup.models.DenominationCountField(default=0, pence_value=500, verbose_name='£5 notes')),
                ('coin_2GBP', cashup.models.DenominationCountField(default=0, pence_value=200, verbose_name='£2 coins')),
                ('coin_1GBP', cashup.models.DenominationCountField(default=0, pence_value=100, verbose_name='£1 coins')),
                ('coin_50p', cashup.models.DenominationCountField(default=0, pence_value=50, verbose_name='50p coins')),
                ('coin_20p', cashup.models.DenominationCountField(default=0, pence_value=20, verbose_name='20p coins')),
                ('coin_10p', cashup.models.DenominationCountField(default=0, pence_value=10, verbose_name='10p coins')),
                ('coin_5p', cashup.models.DenominationCountField(default=0, pence_value=5, verbose_name='5p coins')),
                ('coin_2p', cashup.models.DenominationCountField(default=0, pence_value=2, verbose_name='2p coins')),
                ('coin_1p', cashup.models.DenominationCountField(default=0, pence_value=1, verbose_name='1p coins')),
                ('till_total', models.DecimalField(decimal_places=2, editable=False, max_digits=12)),
                ('till_float', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('till_difference', models.DecimalField(decimal_places=2, max_digits=12)),
                ('notes', models.TextField(blank=True, help_text='Add any useful info here')),
                ('closed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tillclosures', to='cashup.Personnel')),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tillclosures', to='cashup.Outlet')),
            ],
            options={
                'get_latest_by': 'close_time',
                'ordering': ['close_time'],
            },
        ),
        migrations.AddField(
            model_name='outlet',
            name='personnel',
            field=models.ManyToManyField(related_name='outlets', through='cashup.StaffPositions', to='cashup.Personnel'),
        ),
        migrations.AlterUniqueTogether(
            name='staffpositions',
            unique_together=set([('outlet', 'personnel')]),
        ),
        migrations.AlterUniqueTogether(
            name='outlet',
            unique_together=set([('name', 'business')]),
        ),
    ]
