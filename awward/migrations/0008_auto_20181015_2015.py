# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 17:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awward', '0007_auto_20181014_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='rates',
            name='usability',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]