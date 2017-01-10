# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def populate_personnel(apps, schema_editor):
    Personnel = apps.get_model('cashup', 'Personnel')
    User = apps.get_registered_model('auth', 'User')
    for u in User.objects.all():
        is_owner = False
        try:
            business = u.business
        except AttributeError:
            business = u.workplaces.first().business
        else:
            is_owner = True
        Personnel.objects.create(user=u, business=business, is_owner=is_owner)

def populate_staffpositions(apps, schema_editor):
    StaffPositions = apps.get_model('cashup', 'StaffPositions')
    OutletStaff = apps.get_model('cashup', 'OutletStaff')
    for staff in OutletStaff.objects.all():
        StaffPositions.objects.create(
            personnel=staff.user.cashup,
            outlet=staff.outlet,
            is_manager=staff.is_manager
        )


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cashup', '0033_noteshelptext'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnel', to='cashup.Business')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cashup', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffPositions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='outlet',
            old_name='staff',
            new_name='old_staff',
        ),
        migrations.AddField(
            model_name='staffpositions',
            name='outlet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='cashup.Outlet'),
        ),
        migrations.AddField(
            model_name='staffpositions',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='cashup.Personnel'),
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
        migrations.RunPython(populate_personnel, migrations.RunPython.noop),
        migrations.RunPython(populate_staffpositions, migrations.RunPython.noop),
    ]
