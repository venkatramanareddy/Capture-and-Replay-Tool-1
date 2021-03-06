# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='packet_tf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_macaddr', models.CharField(blank=True, max_length=17, null=True)),
                ('dst_macaddr', models.CharField(blank=True, max_length=17, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('src_address', models.CharField(blank=True, max_length=16, null=True)),
                ('dst_address', models.CharField(blank=True, max_length=16, null=True)),
                ('version', models.CharField(blank=True, max_length=2, null=True)),
                ('ihl', models.CharField(blank=True, max_length=2, null=True)),
                ('tos', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('id_IP', models.IntegerField(blank=True, null=True)),
                ('flags', models.CharField(blank=True, max_length=2, null=True)),
                ('frag', models.CharField(blank=True, max_length=2, null=True)),
                ('ttl', models.IntegerField(blank=True, null=True)),
                ('proto', models.IntegerField(blank=True, null=True)),
                ('chksum', models.IntegerField(blank=True, null=True)),
                ('sport', models.IntegerField(blank=True, null=True)),
                ('dport', models.IntegerField(blank=True, null=True)),
                ('seq', models.CharField(blank=True, max_length=11, null=True)),
                ('ack', models.CharField(blank=True, max_length=11, null=True)),
                ('dataofs', models.CharField(blank=True, max_length=2, null=True)),
                ('reserved', models.CharField(blank=True, max_length=2, null=True)),
                ('flags_TCP', models.CharField(blank=True, max_length=2, null=True)),
                ('window', models.IntegerField(blank=True, null=True)),
                ('chksum_TCP', models.IntegerField(blank=True, null=True)),
                ('urgptr', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['pk'],
                'db_table': 'packet',
            },
        ),
        migrations.CreateModel(
            name='trace_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='trace_files/')),
                ('uploaded_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
