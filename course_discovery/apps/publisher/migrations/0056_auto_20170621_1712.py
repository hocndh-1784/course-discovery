# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-21 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0055_auto_20170620_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='full_description_override',
            field=models.TextField(blank=True, default=None, help_text="Full description specific for this run of a course. Leave this value blank to default to the parent course's full_description attribute.", null=True),
        ),
        migrations.AddField(
            model_name='courserun',
            name='title_override',
            field=models.CharField(blank=True, default=None, help_text="Title specific for this run of a course. Leave this value blank to default to the parent course's title.", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='full_description_override',
            field=models.TextField(blank=True, default=None, help_text="Full description specific for this run of a course. Leave this value blank to default to the parent course's full_description attribute.", null=True),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='title_override',
            field=models.CharField(blank=True, default=None, help_text="Title specific for this run of a course. Leave this value blank to default to the parent course's title.", max_length=255, null=True),
        ),
    ]