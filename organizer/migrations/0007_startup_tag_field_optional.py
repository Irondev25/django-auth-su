# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-18 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_newslink_unique_together_slug_startup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='startups', to='organizer.Tag'),
        ),
    ]
