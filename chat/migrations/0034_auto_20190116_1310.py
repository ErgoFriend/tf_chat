# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-16 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0033_auto_20190116_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='status',
            field=models.CharField(choices=[('0', 'テスト'), ('1', '公開')], default='0', max_length=2),
        ),
    ]
