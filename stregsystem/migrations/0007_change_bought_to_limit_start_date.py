# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-27 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stregsystem', '0006_increase_max_length_of_strings_in_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bought',
        ),
        migrations.AddField(
            model_name='product',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
