# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160908_1902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ficicleta',
            new_name='Bicicleta',
        ),
    ]