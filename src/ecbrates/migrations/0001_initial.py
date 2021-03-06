# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-01 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ECBRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField()),
                ('code', models.CharField(max_length=3)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=30)),
            ],
        ),
    ]
