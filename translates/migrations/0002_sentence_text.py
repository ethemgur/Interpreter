# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-09 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='text',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='translates.Text'),
            preserve_default=False,
        ),
    ]
