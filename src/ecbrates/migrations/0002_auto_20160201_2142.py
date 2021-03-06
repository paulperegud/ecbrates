# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-01 21:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecbrates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecbrate',
            name='published',
        ),
        migrations.AddField(
            model_name='ecbrate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 21, 42, 41, 107158, tzinfo=utc), verbose_name='publication date, as defined by ECB'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ecbrate',
            name='code',
            field=models.CharField(max_length=3, verbose_name='target currency code'),
        ),
        migrations.AlterField(
            model_name='ecbrate',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=30, verbose_name='exchange rate'),
        ),
    ]
