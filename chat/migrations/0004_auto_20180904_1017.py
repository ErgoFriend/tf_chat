# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_item_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='userId',
            field=models.CharField(max_length=30, verbose_name='\u30e6\u30fc\u30b6ID'),
        ),
    ]
