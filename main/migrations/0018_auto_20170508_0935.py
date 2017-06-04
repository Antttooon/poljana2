# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170502_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='afisha',
            options={'verbose_name': 'Афиша', 'verbose_name_plural': 'Афиши'},
        ),
        migrations.AlterField(
            model_name='afisha',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Отображать на странице/ не отображать'),
        ),
        migrations.AlterField(
            model_name='maintext',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Отображать на странице/ не отображать'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Отображать на странице/ не отображать'),
        ),
        migrations.AlterField(
            model_name='news',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Отображать на странице/ не отображать'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Отображать на странице/ не отображать'),
        ),
        migrations.AlterField(
            model_name='photo_alboom',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Отображать на странице/ не отображать'),
        ),
        migrations.AlterField(
            model_name='video',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Отображать на странице/ не отображать'),
        ),
    ]
