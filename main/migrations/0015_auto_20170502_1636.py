# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170502_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bg_image',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Использовать как фон'),
        ),
    ]
