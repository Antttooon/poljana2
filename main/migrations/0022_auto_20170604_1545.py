# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 15:45
from __future__ import unicode_literals

import audiofield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_file',
            field=audiofield.fields.AudioField(blank=True, help_text='Allowed type - .mp3, .wav, .ogg', upload_to='audio/%Y/%m/%d/'),
        ),
    ]
