# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-08 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_audioalboom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audioalboom',
            old_name='name',
            new_name='alboom_name',
        ),
        migrations.RemoveField(
            model_name='audiofile',
            name='author',
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='alboom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alboom_namel', to='main.AudioAlboom', verbose_name='Альбом'),
        ),
    ]