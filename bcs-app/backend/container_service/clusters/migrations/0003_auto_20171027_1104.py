# -*- coding: utf-8 -*-
#
# Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
# Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# Generated by Django 1.11.5 on 2017-10-27 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0002_clusterinstalllog_params'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeUpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=64)),
                ('task_id', models.CharField(max_length=64, null=True)),
                ('params', models.TextField()),
                ('is_finished', models.BooleanField(default=False)),
                ('is_polling', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('log', models.TextField()),
                ('cluster_id', models.CharField(max_length=32)),
                ('node_id', models.CharField(max_length=32)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='clusterinstalllog',
            name='is_failed',
        ),
        migrations.AddField(
            model_name='clusterinstalllog',
            name='is_polling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clusterinstalllog',
            name='status',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='clusterinstalllog',
            name='task_id',
            field=models.CharField(max_length=64, null=True),
        ),
    ]