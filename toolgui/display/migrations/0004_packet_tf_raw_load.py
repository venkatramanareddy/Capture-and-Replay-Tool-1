# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20160609_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='packet_tf',
            name='Raw_load',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
