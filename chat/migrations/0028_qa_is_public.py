# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-16 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0027_remove_qa_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa',
            name='is_public',
            field=models.CharField(choices=[('0', 'テスト'), ('1', '公開')], default='0', max_length=1),
        ),
    ]
