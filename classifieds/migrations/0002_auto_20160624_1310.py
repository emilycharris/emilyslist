# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classifieds.Category'),
        ),
    ]
