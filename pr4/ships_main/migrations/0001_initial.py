# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 23:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armaments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArmDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=128)),
                ('service_start_date', models.DateField(blank=True, default='1000-01-01')),
                ('service_end_date', models.DateField(blank=True, default='1000-01-01')),
                ('number_built', models.IntegerField(blank=True, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('calibre', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('recoil', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rate_of_fire', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('velocity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('max_firing_range', models.CharField(blank=True, max_length=256)),
                ('story', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Armour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belt', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('deck', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('barbettes', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('gun_turrets', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('conning_tower', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('bulkheads', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('magazines', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('founded', models.DateField(blank=True, default='1000-01-01')),
                ('defunct', models.DateField(blank=True, default='1000-01-01')),
                ('location', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_data', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Commanders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=128)),
                ('second_name', models.CharField(max_length=128)),
                ('birthdate', models.DateField(blank=True, default='1000-01-01')),
                ('income_date', models.DateField(blank=True, default='1000-01-01')),
                ('withdraw_date', models.DateField(blank=True, default='1000-01-01')),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range1', models.IntegerField(blank=True, null=True)),
                ('speed1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('range2', models.IntegerField(blank=True, null=True)),
                ('speed2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('range3', models.IntegerField(blank=True, null=True)),
                ('speed3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_name', models.CharField(blank=True, max_length=128)),
                ('picture', models.ImageField(max_length=200, upload_to='/ships_main')),
                ('picture_source', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Propulsion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shafts', models.IntegerField(blank=True, null=True)),
                ('steam_turbines', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ship_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('unique_name', models.CharField(max_length=128, unique=True)),
                ('ordered', models.DateField(blank=True, default='1000-01-01')),
                ('laid_down', models.DateField(blank=True, default='1000-01-01')),
                ('launched', models.DateField(blank=True, default='1000-01-01')),
                ('fate', models.DateField(blank=True, default='1000-01-01')),
                ('displacement_norm', models.IntegerField(blank=True)),
                ('displacement_deep', models.IntegerField(blank=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('beam', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('draught', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('speed_surf', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('speed_sub', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('crew_peace', models.IntegerField(blank=True)),
                ('crew_war', models.IntegerField(blank=True)),
                ('story', models.TextField(blank=True, default='', null=True)),
                ('armament', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Armaments')),
                ('armour', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Armour')),
                ('builder', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Builder')),
                ('commanders', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Commanders')),
                ('devices', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Devices')),
                ('endurance', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Endurance')),
                ('pictures', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Pictures')),
                ('power', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='ships_main.Power')),
                ('propulsion', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='ships_main.Propulsion')),
                ('ship_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships_main.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='ship_main',
            name='ship_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ships_main.Type'),
        ),
        migrations.AddField(
            model_name='armdevices',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ships_main.Builder'),
        ),
        migrations.AddField(
            model_name='armaments',
            name='armament_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships_main.ArmDevices'),
        ),
        migrations.AddField(
            model_name='armaments',
            name='ship_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ships_main.ship_main'),
        ),
    ]
