# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20170508_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afisha',
            name='header1',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок 1 ( h4 200 символов)'),
        ),
        migrations.AlterField(
            model_name='afisha',
            name='header2',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок 2 ( h1 200 символов)'),
        ),
        migrations.AlterField(
            model_name='afisha',
            name='header3',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок 3 ( h2 200 символов)'),
        ),
        migrations.AlterField(
            model_name='afisha',
            name='header4',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок 4 ( h3 200 символов)'),
        ),
        migrations.AlterField(
            model_name='afisha',
            name='header5',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок 5 (h4 200 символов)'),
        ),
    ]
