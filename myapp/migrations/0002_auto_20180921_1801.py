# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-21 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='imprint',
            new_name='publisher',
        ),
    ]
