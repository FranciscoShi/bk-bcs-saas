# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-09-15 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20190326_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='k8sloadblance',
            name='namespace',
            field=models.CharField(blank=True, max_length=253, null=True, verbose_name='命名空间名称'),
        ),
        migrations.AlterField(
            model_name='k8sloadblance',
            name='namespace_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mesosloadblance',
            name='namespace_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='k8sloadblance',
            unique_together=set([('cluster_id', 'namespace', 'name')]),
        ),
    ]
