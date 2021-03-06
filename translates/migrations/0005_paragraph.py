# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translates', '0004_sentence_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('tr_content', models.TextField()),
                ('order_id', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translates.Text')),
            ],
        ),
    ]
