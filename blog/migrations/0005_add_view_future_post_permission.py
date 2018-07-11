# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-04 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_field_startups_and_tags_optional'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'pub_date', 'ordering': ['-pub_date', 'title'], 'permissions': (('view_future_post', 'Can View unpublished Post'),), 'verbose_name': 'blog post'},
        ),
    ]
