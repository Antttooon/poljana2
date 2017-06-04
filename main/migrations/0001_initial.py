# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo_Alboom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='albooms/%Y/%m/%d/', verbose_name='Изображение Альбома')),
            ],
            options={
                'verbose_name': 'ФотоАльбом',
                'verbose_name_plural': 'ФотоАльбомы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='lg_photo/%Y/%m/%d/', verbose_name='фотография')),
                ('description', models.TextField(blank=True, verbose_name='Описание фотографии')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('photo_alboom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.Photo_Alboom', verbose_name='Фото Альбом')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
