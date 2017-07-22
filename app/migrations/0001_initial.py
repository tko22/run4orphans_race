# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=2017)),
                ('run_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=5)),
                ('over_18', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('shirt_size', models.IntegerField(default=5)),
                ('gender', models.BooleanField(default=True)),
                ('run_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Run')),
            ],
        ),
    ]
