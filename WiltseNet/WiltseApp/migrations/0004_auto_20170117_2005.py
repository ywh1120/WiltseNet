# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-17 11:05
from __future__ import unicode_literals

import WiltseApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WiltseApp', '0003_auto_20170117_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='uploadfile',
            field=models.FileField(null=True, upload_to=WiltseApp.models.generate_filename, verbose_name='\ucca8\ubd80\ud30c\uc77c'),
        ),
    ]