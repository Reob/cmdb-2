# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]