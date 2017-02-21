# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='league_player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CNName', models.CharField(max_length=100)),
                ('ENName', models.CharField(max_length=100)),
                ('TeamId', models.IntegerField()),
                ('TeamName', models.CharField(max_length=100)),
                ('Number', models.DateTimeField()),
                ('ImageUrl', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('TeamId',),
            },
        ),
        migrations.CreateModel(
            name='league_season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SeasonId', models.IntegerField()),
                ('SeasonName', models.CharField(max_length=100)),
                ('LeagueId', models.IntegerField()),
                ('LeagueName', models.CharField(max_length=100)),
                ('IsHistory', models.BooleanField(default=False)),
                ('BeginTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
            ],
            options={
                'ordering': ('SeasonId',),
            },
        ),
        migrations.CreateModel(
            name='league_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamId', models.IntegerField()),
                ('TeamENName', models.CharField(max_length=100)),
                ('TeamCNName', models.CharField(max_length=100)),
                ('LeagueId', models.IntegerField()),
                ('LeagueName', models.CharField(max_length=100)),
                ('CourtName', models.CharField(max_length=100)),
                ('FoundingTime', models.DateTimeField()),
                ('TeamLogoImage', models.CharField(max_length=100)),
                ('CourtImage', models.CharField(max_length=100)),
                ('Remark', models.TextField()),
                ('UpdateTime', models.DateTimeField(default=1487687599.018823)),
            ],
            options={
                'ordering': ('TeamId',),
            },
        ),
        migrations.CreateModel(
            name='sys_country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryId', models.IntegerField()),
                ('CountryName', models.CharField(max_length=100)),
                ('CountryENName', models.CharField(max_length=100)),
                ('Image', models.CharField(max_length=100)),
                ('InternalName', models.CharField(max_length=100)),
                ('Code', models.DateTimeField()),
            ],
            options={
                'ordering': ('CountryId',),
            },
        ),
        migrations.CreateModel(
            name='sys_league',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LeagueId', models.IntegerField()),
                ('LeagueName', models.CharField(max_length=100)),
                ('ENName', models.CharField(max_length=100)),
                ('CountryId', models.IntegerField()),
                ('CountryName', models.CharField(max_length=100)),
                ('Levels', models.IntegerField()),
                ('TeamCount', models.IntegerField()),
                ('InternalName', models.CharField(max_length=100)),
                ('EventType', models.IntegerField()),
                ('ImageUrl', models.CharField(max_length=100)),
                ('Remark', models.TextField()),
            ],
            options={
                'ordering': ('LeagueId',),
            },
        ),
    ]