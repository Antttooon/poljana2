# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-08 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20170604_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioAlboom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='audio_alboom')),
                ('desc', models.TextField(blank=True, verbose_name='Описание(Не обязательно)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
            ],
        ),
    ]