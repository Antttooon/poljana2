# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_bg_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=200, verbose_name='Заголовок (200 символов)')),
                ('body', models.TextField(blank=True, verbose_name='Текст Новостей')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
            ],
            options={
                'verbose_name_plural': 'Новости',
                'verbose_name': 'Новость',
            },
        ),
        migrations.AlterModelOptions(
            name='bg_image',
            options={'ordering': ['bg'], 'verbose_name': 'Фоновое Изображение', 'verbose_name_plural': 'Фоновые Изображения'},
        ),
        migrations.AlterModelOptions(
            name='maintext',
            options={'ordering': ['text_header'], 'verbose_name': 'Заголовок', 'verbose_name_plural': 'Главный Текст'},
        ),
        migrations.AlterModelOptions(
            name='musician',
            options={'verbose_name': 'Участник Группы', 'verbose_name_plural': 'Участники группы'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['name'], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
