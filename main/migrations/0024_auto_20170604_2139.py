# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-04 21:39
from __future__ import unicode_literals

import audiofield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20170604_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audio_file',
            field=audiofield.fields.AudioField(blank=True, help_text='Allowed type - .mp3, .wav, .ogg', upload_to='audio/'),
        ),
    ]
