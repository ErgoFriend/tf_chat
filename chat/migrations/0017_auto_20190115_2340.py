# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-15 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_auto_20190115_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='qa',
            name='is_public',
            field=models.CharField(choices=[('1', '公開'), ('0', 'テスト')], default='0', max_length=2),
        ),
    ]
