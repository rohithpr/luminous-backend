# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_top', models.CharField(max_length=20)),
                ('resources', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='LocationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminous.Location')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resources', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='locationuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminous.User'),
        ),
    ]
