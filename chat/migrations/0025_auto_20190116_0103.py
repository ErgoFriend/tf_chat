# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-16 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0024_auto_20190116_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='is_public',
            field=models.CharField(choices=[('0', 'テスト'), ('1', '公開')], default='0', max_length=1),
        ),
    ]
