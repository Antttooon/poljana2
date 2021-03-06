# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170425_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=200, verbose_name='Заголовок (200 символов)')),
                ('body', models.TextField(blank=True, verbose_name='Текст Новостей')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
