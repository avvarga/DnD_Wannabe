# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-17 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DnD_app', '0002_character_image_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image_route',
            field=models.CharField(default='', max_length=255),
        ),
    ]
