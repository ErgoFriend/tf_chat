# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_qa_idperuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='Keyword',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
