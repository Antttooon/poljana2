# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-04 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20170604_1545'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Audio',
            new_name='AudioFile',
        ),
    ]
